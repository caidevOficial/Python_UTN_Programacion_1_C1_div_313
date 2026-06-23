personas = [
    {
        "nombre": 'pepe',
        "edad": 56,
        "genero": 'm'
    },
    {
        "nombre": 'moni',
        "edad": 45,
        "genero": 'f'
    },
    {
        "nombre": 'paola',
        "edad": 18,
        "genero": 'f'
    },
]

def es_femenino(persona: dict) -> bool:
    return persona.get('genero') == 'f'

def tiene_edad_56(persona: dict) -> bool:
    return persona.get('edad') == 56

def filtrar_personas(personas: list[dict], callback_filtro):
    filtro = []

    for persona in personas:
        if callback_filtro(persona):
            filtro.append(persona)

    for persona in filtro:
        print(persona)


def agregar_ciudad(persona: dict) -> dict:
    persona.update({'ciudad': 'boedo'})


def mapear_informacion(personas: list[dict], callback_map):

    for indice_persona in range(len(personas)):
        callback_map(personas[indice_persona])
    
    for persona in personas:
        print(persona)

def obtener_edad(persona: dict) -> int:
    return persona.get('edad')

# mapear_informacion(personas, agregar_ciudad)

personas.sort(key=obtener_edad)

for persona in personas:
    print(persona)