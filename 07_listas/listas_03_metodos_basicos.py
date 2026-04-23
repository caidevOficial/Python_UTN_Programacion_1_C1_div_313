# Métodos básicos

# append: agrega el elemento al final de la lista
mi_lista = []
mi_lista.append(45)
mi_lista.append(10)
mi_lista.append(17)
mi_lista.append(19)

# insert: agrega un elemento en la posicion indicada y mueve a la derecha los que le siguen
# insert(indice, valor)
mi_lista.insert(1, 20)

# Si elegimos un índice fuera de rango, como medida de seguridad se agrega al final
mi_lista.insert(100, 9)

# pop: elimina un elemento según su índice
# si no se especifica el índice, elimina el último
mi_lista.pop()
mi_lista.pop(1)

# Si el índice está fuera de rango, se lanza una excepción (error)
# mi_lista.pop(99)  # -> explota

# remove: busca un valor y elimina su -primera- ocurrencia
mi_lista.remove(19)

# Si el elemento no existe en la lista, se lanza una excepción
# mi_lista.remove(-2)  # -> explota

# index: busca un valor y devuelve su índice
elemento_buscado = 10

indice_buscado = mi_lista.index(elemento_buscado)
print(f"El elemento {elemento_buscado} está en el índice {indice_buscado}")

# Si el elemento no existe, se lanza una excepción
# indice_buscado = mi_lista.index(137) # -> explota
