from abc import ABC, abstractmethod
from edge import Edge
from typing import Optional

class RouteCostCalculator(ABC):
    @abstractmethod
    def get_cost(self, edge: Edge) -> Optional[float]:
        """Returns the cost of traversing this edge, or None if it must be excluded entirely."""

class AccessibleRouteCostCalculator(RouteCostCalculator):
    def get_cost(self, edge: Edge) -> Optional[float]:
        #inaccessible edges are excluded entirely (None),
        if not edge.accessible:
            return None
        return edge.horizontal_distance + edge.vertical_distance

class StandardRouteCostCalculator(RouteCostCalculator):
    def get_cost(self, edge: Edge) -> Optional[float]:
        #every edge is usable, cost is just distance (horizontal + vertical).
        return edge.horizontal_distance + edge.vertical_distance