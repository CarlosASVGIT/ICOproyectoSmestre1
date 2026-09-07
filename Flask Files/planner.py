from node import Node
from edge import Edge
from cost_calculator import RouteCostCalculator
from GrafoCETYS import Grafo
import heapq
from typing import Optional

def build_path(parent: dict[Node, Optional[Node]], goal: Node) -> list[Node]:
    """Reconstructs the path."""
    path = [goal]
    while parent[path[-1]] is not None:
        path.append(parent[path[-1]])
    path.reverse()
    return path

class Planner:
    def find_route(
        self,
        graph: Grafo,
        start: Node,
        goal_type: str,
        cost_calculator: RouteCostCalculator,
    ) -> Optional[list[Node]]:
        dist: dict[Node, float] = {node: float('inf') for node in graph.all_nodes()}
        dist[start] = 0.0
        parent: dict[Node, Optional[Node]] = {start: None}
        pq = [(0.0, start.id, start)]

        while pq:
            d, current_id, current = heapq.heappop(pq)

            if current.type == goal_type:
                return build_path(parent, current)

            if d > dist[current]:
                continue

            for edge in graph.get_edges(current):
                cost = cost_calculator.get_cost(edge)
                if cost is None:
                    continue
                neighbor_node = edge.destination
                new_dist = d + cost
                if new_dist < dist.get(neighbor_node, float('inf')):
                    dist[neighbor_node] = new_dist
                    parent[neighbor_node] = current
                    heapq.heappush(pq, (new_dist, neighbor_node.id, neighbor_node))

        return None
