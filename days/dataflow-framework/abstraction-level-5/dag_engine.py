import yaml
from typing import Iterator, Dict, List, Tuple, Callable
from importlib import import_module
from collections import defaultdict
from processor_types import TaggedLine, TaggedProcessor

class DAGNode:
    def __init__(self, name: str, processor: TaggedProcessor):
        self.name = name
        self.processor = processor
        self.children: Dict[str, List[DAGNode]] = defaultdict(list)

def load_dag(config_path: str) -> DAGNode:
    with open(config_path) as f:
        config = yaml.safe_load(f)

    nodes = {}
    for node_cfg in config["nodes"]:
        name = node_cfg["name"]
        module_path, func_name = node_cfg["type"].rsplit(".", 1)
        module = import_module(module_path)
        processor_cls = getattr(module, func_name)
        processor = processor_cls(**node_cfg.get("config", {}))
        nodes[name] = DAGNode(name, processor)

    for route in config["routes"]:
        src = route["from"]
        tag = route["tag"]
        dest = route["to"]
        nodes[src].children[tag].append(nodes[dest])

    return nodes[config["entrypoint"]]

def run_dag(root: DAGNode, lines: Iterator[str]):
    # Map of node name → list of input lines
    node_inputs: Dict[str, List[str]] = defaultdict(list)
    node_inputs[root.name].extend(lines)

    # Lookup from name → DAGNode
    all_nodes = collect_all_nodes(root)

    while node_inputs:
        current_batch = dict(node_inputs)
        node_inputs.clear()

        for node_name, input_lines in current_batch.items():
            node = all_nodes[node_name]
            outputs = node.processor.process(iter(input_lines))
            for tag, line in outputs:
                for child in node.children.get(tag, []):
                    node_inputs[child.name].append(line)

def collect_all_nodes(root: DAGNode) -> Dict[str, DAGNode]:
    visited = {}
    stack = [root]
    while stack:
        node = stack.pop()
        if node.name not in visited:
            visited[node.name] = node
            for children in node.children.values():
                stack.extend(children)
    return visited
