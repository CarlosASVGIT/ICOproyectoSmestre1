from node import Node
from node import Node
from edge import Edge

class Grafo:
    def __init__(self, nodes: list[Node], connections: list[tuple]):

        #connections: lista de tuplas (node_a, node_b, horizontal_distance, vertical_distance, accessible)
       #  tupla genera automáticamente las dos Edges (ida y vuelta).

        self.nodes: dict[str, Node] = {node.id: node for node in nodes}
        self.adjacency: dict[Node, list[Edge]] = {node: [] for node in nodes}

        for a, b, h_dist, v_dist, accessible in connections:
            self.adjacency[a].append(
                Edge(destination=b, horizontal_distance=h_dist,
                     vertical_distance=v_dist, accessible=accessible)
            )
            self.adjacency[b].append(
                Edge(destination=a, horizontal_distance=h_dist,
                     vertical_distance=v_dist, accessible=accessible)
            )

    def get_node(self, node_id: str) -> Node:
        return self.nodes[node_id]

    def all_nodes(self) -> list[Node]:
        return list(self.nodes.values())

    def get_edges(self, node: Node) -> list[Edge]:
        return self.adjacency.get(node, [])
