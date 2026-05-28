supermercado = {"mate", "cafe", "harina"}
tienda_online = {"harina", "palmitos", "yerba"}


supermercado.add("mate-listo")

# print(supermercado)

# supermercado.clear()
# print(supermercado.difference(tienda_online))
# print(supermercado.union(tienda_online))
# print(supermercado.intersection(tienda_online))

print(tienda_online)
# tienda_online.difference_update(supermercado)
# tienda_online.intersection_update(supermercado)
tienda_online.update(supermercado)
tienda_online.discard("Pepsi")
print(tienda_online)


print("mate" in tienda_online)

for elemento in tienda_online:
    print(elemento)

print()

# for indice in range(len(tienda_online)):
#     print(tienda_online[indice])

for indice, elemento in enumerate(tienda_online):
    print(indice, elemento)
