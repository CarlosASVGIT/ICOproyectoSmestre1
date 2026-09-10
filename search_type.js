//Este archivo lo realice con AI, yo implemente la logica, simplemente le dije que lo hiciera porque no conozco sintaxis de JS

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
                opcion16: 'e9'
            };
            return mapaEdificio[edificio];
        }
    }
}

