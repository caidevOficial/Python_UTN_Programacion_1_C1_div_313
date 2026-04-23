# Ejercicio
#
# Le pedimos a un usuario que ingrese 8 números
# y los guardamos en una lista
# Calcular el número máximo de la lista


lista_numeros = []
for i in range(8):
    numero = input("Ingrese un número: ")
    numero_int = int(numero)
    lista_numeros.append(numero_int)


maximo = lista_numeros[0]

for indice in range(1, len(lista_numeros)):
    if lista_numeros[indice] > maximo:
        maximo = lista_numeros[indice]

print(f"La lista es: {lista_numeros}")
print(f"El máximo es: {maximo}")