
def obtener_promedio(lista: list):
    suma = 0
    cantidad = len(lista)
    
    for numero in lista:
        suma += numero
    
    promedio = suma / cantidad
    return promedio


def obtener_porcentaje(cantidad_total: int, cantidad_actual: int) -> float:
    """
    50 -> 100%
    5 -> X? %
    """
    porcentaje = (cantidad_actual * 100) / cantidad_total
    return porcentaje