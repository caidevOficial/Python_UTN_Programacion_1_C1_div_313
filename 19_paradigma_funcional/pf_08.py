vendedores = [
    {
        "vendedor_actual": "PEPE ARGENTO",
        "atenciones_del_dia": 7,
        "ganancias_totales_dia": 50000
    },
    {
        "nombre": "MONI ARGENTO",
        "atenciones_del_dia": 10,
        "ganancias_totales_dia": 75000
    }
]



obtener_nombre = lambda pers: pers.get('nombre')\
                                if 'nombre' in pers.keys()\
                                else pers.get('vendedor_actual')

def obtener_nombre_v2(persona: dict) -> str:
    if 'nombre' in persona.keys():
        return persona.get('nombre')
    
    return persona.get('vendedor_actual')


for persona in vendedores:
    nombre = obtener_nombre(persona)
    print(nombre)