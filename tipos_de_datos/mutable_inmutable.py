edades = [25, 36]
nombre = 'UTN'

print(
    hex(id(edades))
)
edades[0] = 125
print(
    hex(id(edades))
)
print(
    hex(id(nombre))
)
nombre = 'UTN'
print(
    hex(id(nombre))
)
