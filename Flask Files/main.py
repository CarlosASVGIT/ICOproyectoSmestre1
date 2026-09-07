from grafo_data import graph
from cost_calculator import StandardRouteCostCalculator, AccessibleRouteCostCalculator
from planner import Planner

"""
Para probar el script utiliza la terminal de VScode, 
has cd a la carpeta connections y ejecuta 'python3 main.py'
"""

def main():
    planner = Planner()
    start = graph.get_node("floor1_hub_cece")  # hardcoded node of origin
    goal_type = "restroom_f"  # hardcode destination
    accessible_only = True  # hardcoded True/False
    calculator = AccessibleRouteCostCalculator() if accessible_only else StandardRouteCostCalculator()

    route = planner.find_route(graph, start, goal_type, calculator)

    print(start.id, " to ", goal_type, "| Accessibility =", accessible_only)
    if route is None:
        print("No route found.")
    else:
        print(" -> ".join(node.id for node in route))


if __name__ == "__main__":
    main()
