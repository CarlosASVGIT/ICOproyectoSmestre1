//AI me ayudo con este archivo, le di la logica pero no se como vincular JS con html
const nodos = [
    { id: "cafe_vertical", label: "Cafetería Vertical" },
    { id: "floor1_hub_cece", label: "CECE - Piso 1" },
    { id: "floor2_hub_cece", label: "CECE - Piso 2" },
    { id: "floor3_hub_cece", label: "CECE - Piso 3" },
    { id: "floor4_hub_cece", label: "CECE - Piso 4" },
    { id: "idiomas", label: "Departamento de Idiomas" },
    { id: "dvolada", label: "Dvolada" },
    { id: "e1_1", label: "Edificio 1 - Entrada 1" },
    { id: "e1_2", label: "Edificio 1 - Entrada 2" },
    { id: "e1_3", label: "Edificio 1 - Entrada 3" },
    { id: "e2_1", label: "Edificio 2 - Piso 1" },
    { id: "e2_2", label: "Edificio 2 - Piso 2" },
    { id: "e5_1", label: "Edificio 5 - Salon 1" },
    { id: "e5_2", label: "Edificio 5 - Salon 2" },
    { id: "e6", label: "Edificio 6" },
    { id: "e8", label: "Edificio 8" },
    { id: "ed9", label: "Edificio 9" },
    { id: "e9_1", label: "Edificio 9 - Aula 1" },
    { id: "e9_2", label: "Edificio 9 - Aula 2" },
    { id: "bib_entrada", label: "Entrada Biblioteca" },
    { id: "e4_e", label: "Entrada Edificio 4" },
    { id: "n_admin", label: "Nodo Administración" },
    { id: "ncafe", label: "Nodo Cafetería" },
    { id: "of1", label: "Oficina 1" },
    { id: "of2", label: "Oficina 2" },
    { id: "floor2_hub_e4", label: "Piso 2 - Edificio 4" },
    { id: "floor3_hub_e4", label: "Piso 3 - Edificio 4" },
    { id: "floor1_hub_posgrado", label: "Posgrado - Piso 1" },
    { id: "floor2_hub_posgrado", label: "Posgrado - Piso 2" },
    { id: "floor3_hub_posgrado", label: "Posgrado - Piso 3" },
    { id: "PR1", label: "Punto de Reunión 1" },
    { id: "PR2", label: "Punto de Reunión 2" },
    { id: "PR3", label: "Punto de Reunión 3" },
    { id: "ramp4_b", label: "Rampa 4 (Abajo)" },
    { id: "ramp4_t", label: "Rampa 4 (Arriba)" },
    { id: "ramp5_b", label: "Rampa 5 (Abajo)" },
    { id: "ramp5_t", label: "Rampa 5 (Arriba)" },
    { id: "cafe_cece", label: "Saint Coco" },
];

function poblarSelect(selectId) {
    const select = document.getElementById(selectId);
    nodos.forEach(nodo => {
        const opt = document.createElement('option');
        opt.value = nodo.id;
        opt.textContent = nodo.label;
        select.appendChild(opt);
    });
}
poblarSelect('origen');


function mostrarTipoBano() {
    const param1 = document.getElementById('param1').value;
    const contenedorParam3 = document.getElementById('param3-container');
    contenedorParam3.style.display = (param1 === 'opcion3') ? 'block' : 'none';
}

function mostrarEdificio() {
    const param1 = document.getElementById('param1').value;
    const contenedorParam4 = document.getElementById('param4-container');
    contenedorParam4.style.display = (param1 === 'opcion4') ? 'block' : 'none';
}

function actualizarDestino() {
    mostrarTipoBano();
    mostrarEdificio();
}

function obtenerTipoBusqueda() {
    const destino = document.getElementById('param1').value;

    switch (destino) {
        case 'opcion1':
            return 'cafe';

        case 'opcion2':
            return 'meeting_point';

        case 'opcion3': {
            const tipoBano = document.getElementById('param3').value;
            const mapaBano = {
                opcion1: 'restroom_unisex',
                opcion2: 'restroom_m',
                opcion3: 'restroom_f'
            };
            return mapaBano[tipoBano];
        }

        case 'opcion4': {
            const edificio = document.getElementById('param4').value;
            const mapaEdificio = {
                opcion1: 'CECE',
                opcion2: 'posgrado',
                opcion3: 'e8',
                opcion4: 'e1',
                opcion5: 'e2',
                opcion6: 'e4',
                opcion7: 'e5',
                opcion8: 'admin',
                opcion9: 'idiomas',
                opcion10: 'cafe',
                opcion11: 'of1',
                opcion12: 'of2',
                opcion13: 'biblio',
                opcion14: '9000-1',
                opcion15: '9000-2',
                opcion16: 'e9',
                opcion17: 'e6'
            };
            return mapaEdificio[edificio];
        }
    }
}

function buscarMasCercano() {
    const origen = document.getElementById('origen').value;
    const accesible = document.getElementById('param2').value;
    const tipo = obtenerTipoBusqueda();

    fetch('/buscar_mas_cercano', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ origen, tipo, accesible })
    })
    .then(res => res.json())
    .then(data => mostrarRuta(data))
    .catch(err => {
        console.error('Error al buscar:', err);
        mostrarRuta({ error: 'Ocurrió un error al conectar con el servidor.' });
    });
}

function mostrarRuta(data) {
    const contenedor = document.getElementById('resultado-ruta');
    const lista = document.getElementById('lista-pasos');
    lista.innerHTML = '';

    if (data.error) {
        contenedor.style.display = 'block';
        lista.innerHTML = `<li>${data.error}</li>`;
        return;
    }

    data.camino.forEach(id => {
        const li = document.createElement('li');
        li.textContent = id;
        lista.appendChild(li);
    });

    contenedor.style.display = 'block';
}

actualizarDestino();