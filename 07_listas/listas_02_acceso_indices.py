# Índices:    0       1       2       3
mi_lista = ["Axel", "Iván", "Sara", "Sofía"]

# Acceder al segundo elemento (índice 1)
# Se accede usando corchetes [] y el índice
nombre = mi_lista[1]
print(nombre)

# Modificar un elemento accediendo a él
print(mi_lista)

mi_lista[0] = "Julián"

print(mi_lista)

# =================================================
# Si intentamos acceder a un índice fuera de rango
# (mayor al último índice), ocurre un error

# algo = mi_lista[40]
# IndexError: list index out of range