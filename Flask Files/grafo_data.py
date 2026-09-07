from node import Node
from GrafoCETYS import Grafo

n1 = Node(id="n1", type="intersection")
n2 = Node(id="n2", type="intersection")
n3 = Node(id="n3", type="intersection")
n4 = Node(id="n4", type="intersection")
n5 = Node(id="n5", type="intersection")
n6 = Node(id="n6", type="intersection")
n67 = Node(id="n67", type="intersection")
n7 = Node(id="n7", type="intersection")
n8 = Node(id="n8", type="intersection")
n9 = Node(id="n9", type="intersection")
n10 = Node(id="n10", type="intersection")
n11 = Node(id="n11", type="intersection")
n12 = Node(id="n12", type="intersection")
n13 = Node(id="n13", type="intersection")
n14 = Node(id="n14", type="intersection")
n15 = Node(id="n15", type="intersection")
n16 = Node(id="n16", type="intersection")
n17 = Node(id="n17", type="intersection")
n18 = Node(id="n18", type="intersection")
n19 = Node(id="n19", type="intersection")
n20 = Node(id="n20", type="intersection")
n21 = Node(id="n21", type="intersection")
n22 = Node(id="n22", type="intersection")
n23 = Node(id="n23", type="intersection")
n24 = Node(id="n24", type="intersection")
n25 = Node(id="n25", type="intersection")
n26 = Node(id="n26", type="intersection")
n27 = Node(id="n27", type="intersection")
n28 = Node(id="n28", type="intersection")
n29 = Node(id="n29", type="intersection")
n30 = Node(id="n30", type="intersection")
n31 = Node(id="n31", type="intersection")
n32 = Node(id="n32", type="intersection")
n33 = Node(id="n33", type="intersection")
n34 = Node(id="n34", type="intersection")
n35 = Node(id="n35", type="intersection")
n36 = Node(id="n36", type="intersection")
n37 = Node(id="n37", type="intersection")
n38 = Node(id="n38", type="intersection")
n39 = Node(id="n39", type="intersection")
n40 = Node(id="n40", type="intersection")
PR2 = Node(id="PR2", type="meeting_point")
PR1 = Node(id="PR1", type="meeting_point")
PR3 = Node(id="PR3", type="meeting_point")
of1 = Node(id="of1", type="classroom")
of2 = Node(id="of2", type="classroom")
e_admin = Node(id="e_admin", type="classroom")
n_admin = Node(id="n_admin", type="intersection")
bano_admin1 = Node(id="bano_admin1", type="restroom_f")
bano_admin2 = Node(id="bano_admin2", type="restroom_m")
idiomas = Node(id="idiomas", type="classroom")
e5_1 = Node(id="e5_1", type="exit_entrance")
e5_2 = Node(id="e5_2", type="exit_entrance")
e6 = Node(id="e6", type="exit_entrance")
e9 = Node(id="e9", type="exit_entrance")

ramp1_b = Node(id="ramp1_bottom", type="intersection")
ramp1_t = Node(id="ramp1_top", type="intersection")
ramp2_b = Node(id="ramp2_bottom", type="intersection")
ramp2_t = Node(id="ramp2_top", type="intersection")
ramp3_b = Node(id="ramp3_bottom", type="intersection")
ramp3_t = Node(id="ramp3_top", type="intersection")
ramp4_b = Node(id="ramp4_bottom", type="intersection")
ramp4_t = Node(id="ramp4_top", type="intersection")
ramp5_b = Node(id="ramp5_bottom", type="intersection")
ramp5_t = Node(id="ramp5_top", type="intersection")

stairs2_b = Node(id="stairs2_b", type="intersection")
stairs2_t = Node(id="stairs2_t", type="intersection")
stairs3_b = Node(id="stairs3_b", type="intersection")
stairs3_t = Node(id="stairs3_t", type="intersection")
stairs1_b = Node(id="stairs1_b", type="intersection")
stairs1_t = Node(id="stairs1_t", type="intersection")

#EDIFICIOS
e2_1 = Node(id="e2_1", type="exit_entrance")
e2_2 = Node(id="e2_2", type="exit_entrance")
e1_2 = Node(id="e1_2", type="exit_entrance")
e1_1 = Node(id="e1_1", type="exit_entrance")
e8 = Node(id="e8", type="classroom")
e9_2 =Node(id="e9", type="exit_entrance")
e9_1 = Node(id="e9_1", type="exit_entrance")
e7_1 = Node(id="e7_1", type="exit_entrance")
e7_2 = Node(id="e7_2", type="exit_entrance")

#CAFES
dvolada = Node(id="dvolada", type="cafe")

#CAFETERIA
cafe_1 = Node(id="cafe1", type="cafe")
cafe_2 = Node(id="cafe2", type="cafe")
bano_cafeteria = Node(id="bano_cafeteria", type="restroom_unisex")
ncafe = Node(id="ncafe", type="intersection")

#BIBLIOTECA
bib_entrada = Node(id="bib_entrada", type="exit_entrance")
nb1 = Node(id="nb1", type="intersection")
nb2 = Node(id="nb2", type="intersection")
bano_bib1 = Node(id="bano_bib", type="restroom_unisex")
bano_bib2 = Node(id="bano_bib", type="restroom_unisex")



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
cece_1 = Node(id="cece_1", type="exit_entrance")
cece_2 = Node(id="cece_2", type="exit_entrance")

nodes = [n1, n2, n3, n4, n5,n6, n67,n7,n8, n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,
         n20,n21,n22,n23,n24,n25,n26,n27,n28,n29,n30,n31,n32,n3,n34,n35,n36,n37,n38,n39,n40,

         of1, of2,e_admin,n_admin, bano_admin1,
         bano_admin2, idiomas, e5_1, e5_2, e2_1, e1_1, e8, e7_2, e7_1, e6,

        bano_bib2, bano_bib1, bib_entrada, nb1, nb2,


         ramp1_b, ramp1_t,ramp2_b, ramp2_t,ramp3_b, ramp4_b,
         ramp3_t, ramp4_t, ramp5_t, ramp5_b,

         stairs1_b, stairs1_t, stairs2_b, stairs2_t,stairs3_b, stairs3_t,

         cafe_1, cafe_2,ncafe, bano_cafeteria, dvolada,

         floor4_hub_cece, floor3_hub_cece, floor2_hub_cece, floor1_hub_cece,
         elevator_cece, m1_cece, f1_cece, unisex1_cece, cafe_cece, cece_1, cece_2,

         PR2, PR1, PR3
        ]

#conexiones de un nodo a otro, no se tiene que hacer doblemente, en GrafoCETYS se duplican para mantener bidireccionalidad
connections = [
    (n1, n2,10, 0, True),
    (n1, idiomas,5, 0, True),
    (n1, e5_1,10, 0, True),
    (n1, e5_2,5, 0, True),

    (n2, n3,15, 0, True),
    (n2, n5,15, 0, True),

    (n5, n6, 4, 0, True),

    (n5, e_admin,4,0, True),
    (e_admin, n_admin, 10,0,True),
    (n_admin, bano_admin1, 2,0,True),
    (n_admin, bano_admin2, 2,0,True),

    (n6,n67,7,0,True),
    (n67,n7,3,0,True),
    (n7,n8,7,0,True),
    (n7,PR2,10,0,True),
    (PR2, n39, 18, 0, True),
    (n39, n38, 10, 0, True),

    (n3, ramp1_b, 1, 0, True),
    (ramp1_b, ramp1_t, 2, 3, True),
    (ramp1_t, n4,   4, 0, True),

    (n4,of1, 2.5, 0, True),


    (n38, e1_1,15,0,True),
    (n8,ramp5_t,17,0,True),
    (ramp5_t,ramp5_b,2.5, 2.5, True),
    (ramp5_b, n25, 17, 0, True),
    (ramp5_b,n28,10,0,True),
    (n28,n27,5,0,True),
    (n27,n26,5,0,True),
    (n27,e2_1, 25, 0, True),
    (n26,n25,10,0,True),
    (n26,PR3,5,0,True),
    (n25,n24,17,0,True),
    (n25, bib_entrada, 4, 0, True),
    (bib_entrada, nb1, 3.5, 0, True),
    (nb1,nb2, 5, 0, True),
    (nb1, bano_bib1, 3, 0, True),
    (nb2, bano_bib2, 3, 0, True),
    (n24,n23,5,0,True),
    (n23, n22, 30, 0, True),
    (n24,n29,14,0,True),
    (n29,n30,10,0,True),
    (n30,n33, 35,0,True),
    (n30, stairs3_b, 25, 0, False),
    (stairs3_b, stairs3_t, 4, 4, False),
    stairs3_t, e6, 0.5,0,False,
    (n33,n35,15,0,True),
    (n33,n34,25,0,True),
    (n34, e9, 4, 0, True),
    (n35,n36,45,0,True),
    (n36,n37,30,0,True),
    (n37,e1_2, 2.3, 0, True),
    (n37,e9_1,0.5,0,True),
    (e9_2, n36, 0.5,0,True),
    (n31,n40,50,0,True),
    (n40, cece_1, 1.5, 0, True),
    (n40, ramp4_b,1.5,0,True),
    (ramp4_b,ramp4_t,1.5,4,True),
    (ramp4_t,n22,1.5,0,True),
    (n22,n21,25,0,True),
    (n21,n18,10,0,True),
    (n28,stairs1_b, 1,0,False),
    (stairs1_b, stairs1_t, 1, 4, False),
    (stairs1_t, e7_2, 0.5, 0, False),
    (n18,n19,5,0,True),
    (n19,n20,5,0,True),
    (n20,PR1,10,0,True),
    (PR1,n13,10,0,True),
    (n13,n3,25,0,True),
    (n13,ramp2_t,12.5,0,True),
    (ramp2_t,ramp2_b, 1.7, 2, True),
    (ramp2_b,n14, 12.5, 0 , True),
    (n14,n15,4.3,0,True),

    (n15,e8,1.8,0,True),

    (n15,n16,22,0,True),
    (n16,n18,25,0,True),
    (n16, e7_1, 2,0,True),

    (n13, ramp3_b,15,0,True),
    (ramp3_b,ramp3_t,1.5,5,True),
    (ramp3_t,n12,10,0,True),
    (n12, cafe_2, 0.5,0,True),
    (cafe_2,ncafe,11,0,True),
    (ncafe, bano_cafeteria,3,0,True),
    (ncafe,cafe_1,7,0,True),
    (cafe_1, n10, 5, 0,True),
    (n10,n9,4,0,True),
    (n9,n11,6,0,True),
    (n9,n8,13,0,True),
    (n11, dvolada, 3.4,0,True),
    (n11, n12, 13.5,0,True),
    (n23,stairs2_t,7,0,False),
    (stairs2_t,stairs2_b, 5,7,False),
    (stairs2_b,n31,5,0,False),
    (n31,n32,5,0,True),

# edificio CECE
    (cece_2,n32,5,0,True),
    (cece_2, cafe_cece, 4, 0, True),
    (cece_1, floor1_hub_cece, 3, 0, True),
    (cafe_cece, cece_1, 4, 0, True),
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
