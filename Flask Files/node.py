from dataclasses import dataclass
from typing import Literal

@dataclass(frozen=True) #it makes it hashable :3
class Node:
    """
    Es un nodo con un 'id' y un 'type' (e.g. restroom_unisex)
    """
    id: str
    type: Literal["classroom", "restroom_m", "restroom_f", "restroom_unisex",
    "cafe", "meeting_point", "intersection", "exit_entrance", "posgrado", "CECE", "e8",
    "e1", "e2", "e4", "admin", "idiomas", "of1", "of2", "biblio", "9000-1", "9000-2", "e9", "e5", "e6"]

