from abc import ABC, abstractmethod
from edge import Edge
from node import Node 

class RouteCostCalculator(ABC):
    @abstractmethod
    def get_cost(self, edge: Edge) -> float | None:
        """Returns the cost of traversing this edge, or None if it must be excluded entirely."""