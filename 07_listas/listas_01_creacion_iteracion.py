# Crear una lista vacía
mi_lista = []
mi_lista_2 = list()

# Crear una lista con valores iniciales
lista_numeros = [4, 7, 9, 10, 8]
lista_compuesta = ["hola", 7, True, 1.6]

# Recorrer / iterar una lista
cantidad_elementos = len(lista_compuesta)
for indice in range(cantidad_elementos):
    elemento_actual = lista_numeros[indice]
    print(f"Índice N°: {indice} -> elemento: {elemento_actual}")

# =========================================================

# Ejercicio básico: calcular promedio de una lista numérica

lista_numeros = [4, 7, 9, 10, 8]
cantidad_elementos = len(lista_numeros)
suma_total = 0

for indice in range(cantidad_elementos):
    elemento_actual = lista_numeros[indice]
    suma_total += elemento_actual

promedio = suma_total / cantidad_elementos

print(f"El promedio es: {promedio}")