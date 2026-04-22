
def calcular_fibonacci_nro(numero_orden: int) -> int:
    if numero_orden < 2:
        return numero_orden
    else:
        ultimo = numero_orden - 1
        penultimo = numero_orden - 2

        fibo_ultimo = calcular_fibonacci_nro(ultimo)
        fibo_penultimo = calcular_fibonacci_nro(penultimo)

        fibo_actual = fibo_ultimo + fibo_penultimo
        return fibo_actual

if __name__ == '__main__':
    
    ubicacion_usuario = 4
    ubicacion_fibo = ubicacion_usuario - 1

    resultado = calcular_fibonacci_nro(ubicacion_fibo)

    print(f'El {ubicacion_usuario}° num fibonacci es: {resultado}')