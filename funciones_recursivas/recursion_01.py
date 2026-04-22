def calcular_factorial(numero: int) -> int:
    if numero == 1 or numero == 0:
        return 1
    elif numero < 0:
        print('No se puede calcular factorial de un numero negativo.')
        return None
    else:
        num_anterior = numero - 1
        resultado_factorial = numero * calcular_factorial(num_anterior)
        return resultado_factorial

if __name__ == '__main__':

    numero_usuario = int(input('ingrese un numero para calcular el factorial: '))

    resultado = calcular_factorial(numero_usuario)

    print(f'{numero_usuario}! = {resultado}')