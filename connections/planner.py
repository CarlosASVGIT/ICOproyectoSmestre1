from node import Node
from edge import Edge
from cost_calculator import RouteCostCalculator

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
        graph: dict[Node, list[Edge]],
        start: Node,
        goal_type: str,
        cost_calculator: RouteCostCalculator,
    ) -> list[Optional[Node]]:

        dist: dict[Node, float] = {node: float('inf') for node in graph}
        dist[start] = 0.0
        parent: dict[Node, Optional[Node]] = {start: None}  # maps each node to the node that led to it
        pq = [(0.0, start.id, start)]  # (distance, node)

        while pq:
            d, current_id, current = heapq.heappop(pq)

            if current.type == goal_type: # this time it stops searching when it finds a node with the dessired type
                return build_path(parent, current)

            if d > dist[current]: #if this entrey stored distance to that node is worst distance than the best one known, it stops processing this entrey
                continue  
            
            for edge in graph.get(current, []):  # checks each edge connected to the current node
                cost = cost_calculator.get_cost(edge)
                if cost is None: # when it is None it means the edge was inaccessible (e.g. stairs)
                    continue  # skips it

                neighbor_node = edge.destination 
                new_dist = d + cost

                if new_dist < dist.get(neighbor_node, float('inf')): # if the new_dist is better than the previous found path, it overwrites it
                    dist[neighbor_node] = new_dist
                    parent[neighbor_node] = current
                    heapq.heappush(pq, (new_dist,neighbor_node.id, neighbor_node))

        return None  # only runs if no route was found