import funciones as fun
from variables import ARCHIVO_AUTOS, ARCHIVO_HEROES, ARCHIVO_HEROES_2


# dataset = fun.leer_dataset(ARCHIVO_HEROES)
# print(dataset)
# print()

lista = fun.cargar_dataset_sistema(ARCHIVO_HEROES, tipo_outuput_dataset='lista_dict')
matriz = fun.cargar_dataset_sistema(ARCHIVO_HEROES, tipo_outuput_dataset='matrix')
# lista = fun.mapear_ld(lista, ["id", "poder"], int)
# lista = fun.mapear_ld(lista, ["altura_mts", "peso_kg"], float)


# print(matriz)
# print()

cabecera = 'id,nombre,identidad,alias,inteligencia,fuerza,velocidad,poder,genero,raza,altura_mts,peso_kg,color_ojos,color_pelo,alineacion,empresa'
config = {
    "data": lista,
    "auto_header": True,
    "path": ARCHIVO_HEROES_2
}


fun.guardar_dataset_csv_v2(config)
# print(lista)
