from graph import Graph

g = Graph()
g.add_node(1, "A")
g.add_node(2,"B")
g.add_node(3, "C")
g.add_node(4,"D")
g.add_edge(1,2,3.3)
g.add_edge(2,3)

# Serialize
json_data = g.to_json()
print("Serialized Graph JSON:")
print(json_data)

# Deserialize
g2 = Graph.from_json(json_data)
print("Deserialized Graph JSON:")
for node_id, node in g2.nodes.items():
    print(f"Node {node_id}: {node.label}")
for edge in g2.edges:
    print(f"Edge from {edge.from_node} to {edge.to_node} with weight {edge.weight}")