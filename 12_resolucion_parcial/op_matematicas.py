
def obtener_promedio(lista_num: list) -> float:
    cantidad = len(lista_num)
    suma = 0
    for num in lista_num:
        suma += num
    
    if cantidad == 0:
        return 0
    return suma / cantidad

def obtener_mayor(lista_num: list) -> int:
    mayor = None

    for elemento in lista_num:
        if mayor == None or elemento > mayor:
            mayor = elemento
    return mayor

def obtener_porcentaje(lista_cond: list, valor: str) -> float:
    cantidad = len(lista_cond)
    cantidad_cumple = 0

    for elemento in lista_cond:
        if elemento == valor:
            cantidad_cumple += 1
    porcentaje = cantidad_cumple * 100 / cantidad
    return porcentaje