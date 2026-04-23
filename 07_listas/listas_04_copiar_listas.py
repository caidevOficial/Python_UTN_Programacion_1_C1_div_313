# Copiar listas

# en este caso, lista_copia no está almacenando los valores de
# lista_original, sino que almacena su referencia (dirección de memoria)
lista_original = [4, 7, 8, 6]
lista_copia = lista_original

print(f"La lista original es: {lista_original}") # imprime [4, 7, 8, 6]
print(f"La lista copiada es: {lista_copia}") # imprime [4, 7, 8, 6]

# Modificamos la lista original
lista_original[0] = 100

print(f"La lista original es: {lista_original}") # imprime [100, 7, 8, 6]
print(f"La lista copiada es: {lista_copia}")  # imprime [100, 7, 8, 6]

# Aunque solo hayamos modificado la lista original sin tocar la copia,
# ambas resultan modificadas

# ============================================================================

# Forma correcta de copiar una lista

lista_original = [4, 7, 8, 6]
lista_copia = []

# Creamos una lista vacía y vamos agregando los valores uno por uno
# de la lista original

for indice in range (len(lista_original)): 
    lista_copia.append(lista_original[indice])

    
print(f"La lista original es: {lista_original}") # imprime [4, 7, 8, 6]
print(f"La lista copiada es: {lista_copia}") # imprime [4, 7, 8, 6]

lista_original[0] = 100

print(f"La lista original es: {lista_original}") # imprime [100, 7, 8, 6]
print(f"La lista copiada es: {lista_copia}") # imprime [4, 7, 8, 6]

