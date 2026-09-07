from node import Node
from edge import Edge

def build_building_graph() -> dict[Node, list[Edge]]:
    floor4_hub_cece = Node(id="floor4_hub_cece", type="intersection")
    floor3_hub_cece = Node(id="floor3_hub_cece", type="intersection")
    floor2_hub_cece = Node(id="floor2_hub_cece", type="intersection")
    floor1_hub_cece = Node(id="floor1_hub_cece", type="intersection")

    elevator_cece = Node(id="elevator_cece", type="intersection")

    m1_cece = Node(id="restroom_m_cece", type="restroom_m")
    f1_cece = Node(id="restroom_f_cece", type="restroom_f")
    unisex1_cece = Node(id="restroom_unisex_cece", type="restroom_unisex")
    cafe_cece = Node(id="cafe_cece", type="cafe")

    graph: dict[Node, list[Edge]] = {
        floor4_hub_cece: [
            Edge(destination=m1_cece, horizontal_distance=5, vertical_distance=0, accessible=True),
            Edge(destination=floor3_hub_cece, horizontal_distance=10, vertical_distance=6, accessible=False),  # stairs
            Edge(destination=elevator_cece, horizontal_distance=15, vertical_distance=0, accessible=True),
        ],
        floor3_hub_cece: [
            Edge(destination=f1_cece, horizontal_distance=5, vertical_distance=0, accessible=True),
            Edge(destination=floor4_hub_cece, horizontal_distance=10, vertical_distance=6, accessible=False),
            Edge(destination=floor2_hub_cece, horizontal_distance=10, vertical_distance=6, accessible=False),
            Edge(destination=elevator_cece, horizontal_distance=15, vertical_distance=0, accessible=True),
        ],
        floor2_hub_cece: [
            Edge(destination=unisex1_cece, horizontal_distance=5, vertical_distance=0, accessible=True),
            Edge(destination=floor3_hub_cece, horizontal_distance=10, vertical_distance=6, accessible=False),
            Edge(destination=floor1_hub_cece, horizontal_distance=10, vertical_distance=6, accessible=False),
            Edge(destination=elevator_cece, horizontal_distance=15, vertical_distance=0, accessible=True),
        ],
        floor1_hub_cece: [
            Edge(destination=cafe_cece, horizontal_distance=5, vertical_distance=0, accessible=True),
            Edge(destination=floor2_hub_cece, horizontal_distance=10, vertical_distance=6, accessible=False),
            Edge(destination=elevator_cece, horizontal_distance=15, vertical_distance=0, accessible=True),
        ],
        elevator_cece: [
            Edge(destination=floor4_hub_cece, horizontal_distance=15, vertical_distance=0, accessible=True),
            Edge(destination=floor3_hub_cece, horizontal_distance=15, vertical_distance=0, accessible=True),
            Edge(destination=floor2_hub_cece, horizontal_distance=15, vertical_distance=0, accessible=True),
            Edge(destination=floor1_hub_cece, horizontal_distance=15, vertical_distance=0, accessible=True),
        ],
        
        m1_cece: [Edge(destination=floor1_hub_cece, horizontal_distance=5, vertical_distance=0, accessible=True)],
        f1_cece: [Edge(destination=floor2_hub_cece, horizontal_distance=5, vertical_distance=0, accessible=True)],
        unisex1_cece: [Edge(destination=floor3_hub_cece, horizontal_distance=5, vertical_distance=0, accessible=True)],
        cafe_cece: [Edge(destination=floor4_hub_cece, horizontal_distance=5, vertical_distance=0, accessible=True)],
        
    }
    return graph