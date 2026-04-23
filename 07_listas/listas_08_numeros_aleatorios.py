import random

# ingresar 10 números aleatorios
lista = []
for i in range(10):
    # randint toma un numero entero entre los 2 límites especificados
    # incluye a ambos
    numero_aleatorio = random.randint(5, 10)
    # randrange es similar pero no incluye al límite superior (similar a range())
    # numero_aleatorio = random.randrange(5, 10)
    lista.append(numero_aleatorio)

print(lista)