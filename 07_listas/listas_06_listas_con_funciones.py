# Ejercicio: crear una funcion que tome una lista de números
# y que devuelva una nueva lista con los números pares que contiene

def obtener_numeros_pares(lista: list) -> list:
    numeros_pares = []
    for indice in range(len(lista)):
        numero = lista[indice]
        if numero % 2 == 0:
            numeros_pares.append(numero)

    return numeros_pares


mi_lista = [1, 5, 8, 6, 3, 10, 5, 12]
nueva_lista = obtener_numeros_pares(mi_lista)

print(f"La lista original es: {mi_lista}")
print(f"Los numeros pares son: {nueva_lista}")