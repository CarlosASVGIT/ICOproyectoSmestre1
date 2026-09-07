from node import Node
from GrafoCETYS import Grafo

n1 = Node(id="n1", type="intersection")
n2 = Node(id="n2", type="intersection")
n3 = Node(id="n3", type="intersection")
n4 = Node(id="n4", type="intersection")
n5 = Node(id="n5", type="intersection")
n6 = Node(id="n6", type="intersection")
of1 = Node(id="of1", type="classroom")
of2 = Node(id="of2", type="classroom")
e_admin = Node(id="e_admin", type="classroom")
n_admin = Node(id="n_admin", type="intersection")
bano_admin1 = Node(id="bano_admin1", type="restroom_f")
bano_admin2 = Node(id="bano_admin2", type="restroom_m")
idiomas = Node(id="idiomas", type="classroom")
e5_1 = Node(id="e5_1", type="exit_entrance")
e5_2 = Node(id="e5_2", type="exit_entrance")
ramp1_b = Node(id="ramp1_bottom", type="intersection")
ramp1_t = Node(id="ramp1_top", type="intersection")

# NODOS CECE
floor4_hub_cece = Node(id="floor4_hub_cece", type="intersection")
floor3_hub_cece = Node(id="floor3_hub_cece", type="intersection")
floor2_hub_cece = Node(id="floor2_hub_cece", type="intersection")
floor1_hub_cece = Node(id="floor1_hub_cece", type="intersection")
m1_cece = Node(id="restroom_m_cece", type="restroom_m")
f1_cece = Node(id="restroom_f_cece", type="restroom_f")
unisex1_cece = Node(id="restroom_unisex_cece", type="restroom_unisex")
cafe_cece = Node(id="cafe_cece", type="cafe")
elevator_cece = Node(id="elevator_cece", type="intersection")

nodes = [n1, n2, n3, n4, n5,n6, of1, of2,e_admin,n_admin, bano_admin1,
         bano_admin2, idiomas, e5_1, e5_2, ramp1_b, ramp1_t,
         floor4_hub_cece, floor3_hub_cece, floor2_hub_cece, floor1_hub_cece,
         elevator_cece, m1_cece, f1_cece, unisex1_cece, cafe_cece
        ]

connections = [
    (n1, n2,10, 0, True),
    (n1, idiomas,5, 0, True),
    (n1, e5_1,10, 0, True),
    (n1, e5_2,5, 0, True),
    (n2, n3,15, 0, True),
    (n2, n5,15, 0, True),
    (n3, ramp1_b, 1, 0, True),
    (ramp1_b, ramp1_t, 2, 3, True),
    (ramp1_t, n4,   4, 0, True),
    (n4,of1, 2.5, 0, True),
    (n4,of2, 2.5,0,True),
    (n5, n6, 4,0, True),
    (n5, e_admin,4,0, True),
    (e_admin, n_admin, 10,0,True),
    (n_admin, bano_admin1, 2,0,True),
    (n_admin, bano_admin2, 2,0,True),
# edificio CECE
    (floor4_hub_cece, m1_cece, 5, 0, True),
    (floor3_hub_cece, f1_cece, 5, 0, True),
    (floor2_hub_cece, unisex1_cece, 5, 0, True),
    (floor1_hub_cece, cafe_cece, 5, 0, True),
    (floor4_hub_cece, floor3_hub_cece, 10, 6, False),
    (floor3_hub_cece, floor2_hub_cece, 10, 6, False),
    (floor2_hub_cece, floor1_hub_cece, 10, 6, False),
    (elevator_cece, floor4_hub_cece, 15, 0, True),
    (elevator_cece, floor3_hub_cece, 15, 0, True),
    (elevator_cece, floor2_hub_cece, 15, 0, True),
    (elevator_cece, floor1_hub_cece, 15, 0, True)
]

graph = Grafo(nodes=nodes, connections=connections)
