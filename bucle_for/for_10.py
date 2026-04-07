"""
Se ingresan un máximo de 10 números o 
hasta que el usuario ingrese el número 0. 
Mostrar la suma y el promedio de todos los números.
"""

num_ingresado = 0
acumulador = 0
promedio = 0
limite = 10
contador = 0

for vuelta in range(limite):

    num_ingresado = int(input('ingrese un número: '))
    acumulador += num_ingresado


    if num_ingresado == 0:
        break
    
    contador += 1

if contador == 0:
    promedio = None
else:
    promedio = acumulador / contador

mensaje =\
f"""
Suma total: {acumulador}
Cantidad Nums: {contador}
Promedio: {promedio}
"""
print(mensaje)