from flask import Flask, render_template, request, jsonify
from planner import Planner
from cost_calculator import AccessibleRouteCostCalculator, StandardRouteCostCalculator
from grafo_data import graph

app = Flask(__name__)
planner = Planner()

@app.route('/')
def mapa():
    return render_template('map.html')


@app.route('/buscar_mas_cercano', methods=['POST'])
def buscar_mas_cercano():
    data = request.get_json() #AI me ayudo con los archivos json, yo realice la logica
    origen_id = data.get('origen')
    tipo = data.get('tipo')
    accesible = data.get('accesible')

    start_node = graph.get_node(origen_id)
    if start_node is None:
        return jsonify({"error": f"Nodo de origen '{origen_id}' no encontrado"}), 400

    if accesible == 'valorB':
        cost_calculator = AccessibleRouteCostCalculator()
    else:
        cost_calculator = StandardRouteCostCalculator()

    path = planner.find_route(graph, start_node, tipo, cost_calculator)

    if path is None:
        return jsonify({"error": "No se encontró una ruta"}), 404 #AI me ayudo con los archivos json, yo realice la logica

    return jsonify({
        "camino": [node.name for node in path]
    })

app.run(debug=True)