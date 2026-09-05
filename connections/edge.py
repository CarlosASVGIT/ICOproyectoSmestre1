from node import Node
from dataclasses import dataclass 

@dataclass
class Edge:
    destination: Node
    horizontal_distance: float
    vertical_distance: float
    accessible: bool