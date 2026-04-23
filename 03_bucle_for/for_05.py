
"""
iterar numeros hasta que aparezca un numero que
sea multiplo 10 y al mismo tiempo multiplo de 5
Cuando se encuentre, mostrarlo y dejar de iterar
"""

for numero in range(11, 1000, 1):
    if numero % 5 == 0 and numero % 10 == 0:
        print(f'{numero} es multiplo de 5 y de 10')
        break

print('Bucle terminado')