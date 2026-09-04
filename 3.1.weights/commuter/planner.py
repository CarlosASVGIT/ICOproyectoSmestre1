from dataclasses import dataclass
from pprint import pprint
from collections import deque


from commuter.cost import TripCostCalculator
from commuter.roads import MapService


@dataclass
class Plan:
    route: list[str]
    cost: float


class TripPlanner:
    def __init__(self, map_service: MapService, cost_calculator: TripCostCalculator):
        self.map_service: MapService = map_service
        self.cost_calculator: TripCostCalculator = cost_calculator

    def plan_route(self, origin: str, destination: str) -> Plan:
        """
        Plans a route from the origin to the destination and returns a Plan object
        containing the route and its associated cost.
        Raises a ValueError if no route is found between the origin and destination.
        """
        city_map = self.map_service.create_city_map()

        stack = deque([origin])
        visited, parent = {origin}, {origin: None}

        while stack:
            if (node := stack.popleft()) == destination:
                path = [destination]
                while parent[path[-1]] is not None:
                    path.append(parent[path[-1]])
                path.reverse()
                return Plan(route=path, cost=self.cost_calculator.get_cost(path))
            for neighbor in city_map.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    stack.append(neighbor)

        raise ValueError(f"No route found")
