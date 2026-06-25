

multiplicar = lambda numero_1, numero_2: numero_1 * numero_2
def multiplicar_v2(numero_1: int, numero_2: int) -> int:
    return numero_1 * numero_2

persona = {
    "nombre": 'pepa',
    "genero": 'f'
}

vendedores = [
    {
        "vendedor_actual": "PEPE ARGENTO",
        "atenciones_del_dia": 7,
        "ganancias_totales_dia": 50000
    },
    {
        "vendedor_actual": "MONI ARGENTO",
        "atenciones_del_dia": 10,
        "ganancias_totales_dia": 75000
    }
]

es_masculino = lambda persona_dict: persona_dict.get('genero') == 'm'

def es_masculino_v2(persona: dict) -> bool:
    return persona.get('genero') == 'm'

# print(
#     # es_masculino(persona)
#     multiplicar_v2('argento', 'pepe ')
# )

def obtener_ganancias_del_dia(vendedor: dict) -> float:
    return vendedor.get('ganancias_totales_dia')

def mapear_informacion(personas: list[dict], callback_map):

    for indice_persona in range(len(personas)):
        res = callback_map(personas[indice_persona])
        print(res, personas[indice_persona].get('vendedor_actual'))
    
    # for persona in personas:
    #     print(persona)

def agregar_ciudad(persona: dict) -> dict:
    persona.update({'ciudad': 'boedo'})

vendedores.sort(key=lambda vend: vend.get('ganancias_totales_dia'))

# NO HACER ESTE MAMARRACHO
actualizar_ciudad = lambda vend: vend.update({'ciudad': 'boedo'})\
                    if vend.get('vendedor_actual') == 'MONI ARGENTO'\
                    else 'm' if type(vend) == dict else None

mapear_informacion(vendedores, actualizar_ciudad)
print(vendedores)

# if persona.get('genero') == 'f':
#     genero = 'f'
# else:
#     genero = 'm'

# genero = 'f' if persona.get('genero') == 'f' else 'm'
# print(genero)