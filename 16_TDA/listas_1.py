
numeros = [
    4,7,2,5
]

precios = [
    45,90,100.75, 900.34, 100
]

for numero, precio in zip(precios, numeros):
    print(f'{numero} - {precio}')