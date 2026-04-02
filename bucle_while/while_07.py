nombre: str = None

while nombre == None or not nombre.isalpha():
    nombre = input('Ingrese su nombre: ')

print(f'Bienvenido: {nombre}')
