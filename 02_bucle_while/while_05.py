maximo = None
minimo = None
nombre_minimo = None
nombre_maximo = None
cant_numeros_totales = 5
cant_numero_actual = 0

while cant_numero_actual < cant_numeros_totales:

    numero_actual = input('Ingrese su edad: ')
    numero_actual_int = int(numero_actual)

    nombre = input('Ingrese su nombre: ')

    # maximo
    if maximo == None or numero_actual_int > maximo:
        maximo = numero_actual_int
        nombre_maximo = nombre

    if minimo == None or numero_actual_int < minimo:
        minimo = numero_actual_int
        nombre_minimo = nombre
    
    cant_numero_actual += 1

mensaje =\
f'''
Cantidad de numeros: {cant_numero_actual}
Máximo: {maximo} - Nombre: {nombre_maximo}
Mínimo: {minimo} - Nombre: {nombre_minimo}
'''
print(mensaje)