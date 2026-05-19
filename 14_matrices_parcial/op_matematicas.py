
def obtener_promedio(matriz: list[list], indice_fila: int):

    suma = 0
    cantidad_elm = len(matriz[indice_fila])

    for valor in matriz[indice_fila]:
        suma += valor
    
    promedio = suma / cantidad_elm
    return promedio

def obtener_promedio_t(matriz: list[list], indice_col: int):
    suma = 0
    cantidad_elm = len(matriz)

    for fila in matriz:
        suma += fila[indice_col]
    promedio = suma / cantidad_elm
    return promedio

def obtener_mayor(matriz: list[list], indice_fila: int) -> int:
    lista_a_iterar = matriz[indice_fila]
    mayor = None

    for elemento in lista_a_iterar:
        if elemento == None or mayor < elemento:
            mayor = elemento
    
    return mayor

def obtener_mayor_vt(matriz: list[list], indice_col: int) -> int:
    mayor = None

    for fila in matriz:
        elemento_actual = fila[indice_col]
        if mayor == None or elemento_actual > mayor:
            mayor = elemento_actual
    
    return mayor

def obtener_porcentaje(matriz: list[list], indice_col: int, valor: str) -> float:
    cantidad = len(matriz)
    cantidad_actual = 0

    for fila in matriz:
        if fila[indice_col] == valor:
            cantidad_actual += 1
    porcentaje = cantidad_actual * 100 / cantidad
    return porcentaje