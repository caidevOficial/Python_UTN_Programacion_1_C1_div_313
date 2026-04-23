# Ejercicio
#
# Crear una funcion que tome una lista de numeros
# y elimine los numeros mayores o iguales a 10
# (eliminarlos de la lista original sin crear una nueva)

def eliminar_numeros_mayores_error(lista_numeros: list) -> None:
    # En un principio podríamos pensar esto
    cantidad_elementos = len(lista_numeros)
    for indice in range(cantidad_elementos):
        numero = lista_numeros[indice]
        if numero >= 10:
            # al hacer .pop(), se reduce en 1 el tamaño de la lista
            lista_numeros.pop(indice)
    # El problema es que estamos modificando el tamaño de la lista
    # a medida que la recorremos, por lo que en algún momento vamos
    # a intentar acceder a un índice fuera de rango y ocurrirá un error
    return None

# Una posible solución es iterar la lista de atrás hacia adelante
def eliminar_numeros_mayores(lista_numeros: list) -> None:
    ultimo_indice = len(lista_numeros) - 1
    for indice in range(ultimo_indice, -1, -1):
        numero = lista_numeros[indice]
        if numero >= 10:
            lista_numeros.pop(indice)
    return None

lista = [100, 8, 66, 4, 14, 22, 3, 6, 8, 11]
print(f"Lista inicial: {lista}")
eliminar_numeros_mayores(lista)
print(f"Lista final: {lista}")