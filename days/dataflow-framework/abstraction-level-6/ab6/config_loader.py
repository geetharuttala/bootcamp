import yaml
import importlib
import networkx as nx

def load_config(path):
    with open(path) as f:
        raw = yaml.safe_load(f)

    processors = {}
    graph = nx.DiGraph()

    for node in raw["nodes"]:
        tag = node["tag"]
        dotted_path = node["type"]
        module_path, func_name = dotted_path.rsplit(".", 1)
        module = importlib.import_module(f"ab6.{module_path}")
        processor = getattr(module, func_name)
        processors[tag] = processor
        graph.add_node(tag)

    # Connect edges based on simulated outputs (deferred for dynamic analysis)
    return {
        "processors": processors,
        "start": "start",
        "graph": graph,
    }
