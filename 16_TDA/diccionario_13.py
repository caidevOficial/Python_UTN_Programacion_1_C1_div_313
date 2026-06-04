alumnos = [
    {
        "id": 10,
        "nombre": 'JuanPa',
        "provincia": 'Buenos Aires',
        "estado": 'graduado'
    },
    {
        "id": 25,
        "nombre": 'Facu',
        "provincia": 'Cordoba',
        "estado": 'graduado'
    },
    {
        "id": 100,
        "nombre": 'Pepe',
        "provincia": 'Buenos Aires',
        "estado": 'en curso'
    }
]

materias = [
    {
        "id": 101,
        "nombre": "Progra I",
        "horas": 8
    },
    {
        "id": 102,
        "nombre": "Progra II",
        "horas": 8
    },
    {
        "id": 103,
        "nombre": "Progra III",
        "horas": 8
    },
    {
        "id": 104,
        "nombre": "Progra IV",
        "horas": 8
    }
]

estado_cursada = []

# id,nombre,horas
# id,nombre,provincia,estado
from listas_3 import join_lista_a_texto

def obtener_encabezado(lista_datos: list[dict]):
    primer_elemento = lista_datos[0]
    claves = primer_elemento.keys()
    columnas = list(claves)
    texto_nombre_columnas = join_lista_a_texto(columnas, ',')
    return texto_nombre_columnas

def obtener_informacion_lista(lista_datos: list[dict], nombre_columnas: str):
    datos = f'{nombre_columnas}'

    for dato in lista_datos:
        datos_lista = list(dato.values())
        info_texto = join_lista_a_texto(datos_lista, ',')
        datos = f'{datos}\n{info_texto}'
    return datos

def mostrar_info_listas(lista_datos: list[dict]):
    nombre_columnas = obtener_encabezado(lista_datos)
    datos = obtener_informacion_lista(lista_datos, nombre_columnas)
    print(datos)



from utn_fra_datasets.datasets import lista_dict_pokemones

mostrar_info_listas(alumnos)
id_alumno = int(input('Ingrese el id de un pokemon: '))
print()
mostrar_info_listas(materias)
id_materia = int(input('Ingrese el id de una materia: '))

# {"id": 1, "id_alumno": 10, "id_materia": 101}
datos_registro = {"id": 1, "id_alumno": id_alumno, "id_materia": id_materia}
estado_cursada.append(datos_registro)
datos_registro = {"id": 2, "id_alumno": id_alumno, "id_materia": id_materia+1}
estado_cursada.append(datos_registro)

print(estado_cursada)

facturas = [{'id_factura': 100, 'id_comprador': 10, 'id_carrito': 4}]

productos = [
    {
        "id_p": 1,
        "precio_unit": 100
    },
    {
        "id_p": 2,
        "precio_unit": 150
    }
]

carritos = [
    {
        'id': 4,
        'id_productos': [
            1,1, 5,5,5,5, 10, 30, 45,45,
            #(id_prod, cantidad)
            (1, 2), (5, 4), (10, 1)
        ]
    }
]

carrito_v2 = [
    {'id':1, 'id_carrito': 4, 'id_producto': 5, 'cantidad': 4},
    {'id':2, 'id_carrito': 4, 'id_producto': 10, 'cantidad': 1},
    {'id':3, 'id_carrito': 4, 'id_producto': 1, 'cantidad': 2}
]

# buscaria los ids unicos de cada producto (set)
# por cada id, contaria la cantidad de unidades
# extraigo valor unit y multiplico por unidades para saber sub_total
# sumo subtotales para tener total del carrito