from node import Node
from dataclasses import dataclass 

@dataclass
class Edge:
    """
    La cosa que conecta dos nodos diferentes;
    destination, horizontal_distance, vertical_distance, accessible
    """
    destination: Node
    horizontal_distance: float
    vertical_distance: float
    accessible: bool