# ab6/router_engine.py

import yaml
import networkx as nx
import matplotlib.pyplot as plt
from importlib import import_module
from typing import Callable, Iterator
from .common.types import TaggedLine

Processor = Callable[[Iterator[TaggedLine]], Iterator[TaggedLine]]

def load_config(config_path) -> dict:
    with open(config_path) as f:
        config = yaml.safe_load(f)

    tag_to_processor = {}
    graph = nx.DiGraph()

    for node in config["nodes"]:
        tag = node["tag"]
        module_path, func_name = node["type"].rsplit(".", 1)
        module = import_module(module_path)
        processor_func = getattr(module, func_name)
        tag_to_processor[tag] = processor_func
        graph.add_node(tag)

    # Pre-declare configured edges
    for edge in config.get("edges", []):
        graph.add_edge(edge["from"], edge["to"])

    return {
        "processors": tag_to_processor,
        "graph": graph,
        "start": config["nodes"][0]["tag"]
    }

def run_router(config: dict, lines: Iterator[str], visualize=False):
    processors = config["processors"]
    graph = config["graph"]
    start_tag = config["start"]

    # Initial tagged output from start processor
    streams: dict[str, list[TaggedLine]] = {
        start_tag: list(processors[start_tag](lines))
    }
    active_tags = [start_tag]

    while active_tags:
        next_active_tags = []
        for tag in active_tags:
            if tag not in processors:
                continue

            processor = processors[tag]
            input_lines = (
                iter(line for _, line in streams.get(tag, []))
                if tag == start_tag else
                iter(streams.get(tag, []))
            )

            # Defensive fallback if processor returns None
            raw_output = processor(input_lines)
            if raw_output is None:
                output_lines = []
            else:
                output_lines = list(raw_output)

            for out_tag, out_line in output_lines:
                if out_tag not in processors:
                    raise ValueError(f"Tag '{out_tag}' is emitted but not registered in config!")

                graph.add_edge(tag, out_tag)
                if not nx.is_directed_acyclic_graph(graph):
                    raise RuntimeError(f"Cycle detected: {tag} → {out_tag}")

                if out_tag not in streams:
                    streams[out_tag] = []
                streams[out_tag].append((out_tag, out_line))
                if out_tag not in next_active_tags:
                    next_active_tags.append(out_tag)

        active_tags = next_active_tags

    if visualize:
        visualize_graph(graph)

def visualize_graph(graph: nx.DiGraph, path: str = "routing_graph.png"):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(graph, seed=42)
    nx.draw(
        graph, pos, with_labels=True,
        node_color="lightblue", edge_color="gray",
        node_size=2000, font_size=10, font_weight='bold'
    )
    nx.draw_networkx_edge_labels(graph, pos, edge_labels={(u, v): "" for u, v in graph.edges()})
    plt.title("Routing Flow Graph")
    plt.tight_layout()
    plt.savefig(path)
    print(f"Routing graph saved to {path}")
