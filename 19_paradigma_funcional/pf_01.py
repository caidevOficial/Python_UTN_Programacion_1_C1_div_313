

def sumar(numero_1: int, numero_2: int) -> int:
    """
    Suma dos numeros
    Args:
        numero_1: ....
        numero_2: ....
    Retuns:
        La suma de ambos numeros
    """
    return numero_1 + numero_2

def restar(numero_1: int, numero_2: int) -> int:
    """
    Resta dos numeros
    Args:
        numero_1: ....
        numero_2: ....
    Retuns:
        La suma de ambos numeros
    """
    return numero_1 - numero_2

def multiplicar(numero_1: int, numero_2: int) -> int:
    """
    Multiplica dos numeros
    Args:
        numero_1: ....
        numero_2: ....
    Retuns:
        La suma de ambos numeros
    """
    return numero_1 * numero_2

def dividir(numero_1: int, numero_2: int) -> int:
    """
    Divide dos numeros
    Args:
        numero_1: ....
        numero_2: ....
    Retuns:
        La suma de ambos numeros
    """
    return numero_1 / numero_2

def operar(numero_1: int, numero_2: int, callback) -> int | float:
    resultado = callback(numero_1, numero_2)
    return resultado

op_matematicas = {
    "suma": sumar,
    "resta": restar,
    "mul": multiplicar,
    "div": dividir
} 


numero_1 = 10
numero_2 = 20


eleccion = input('Elegi entre suma, resta, mul, div: ')

print(f'Operacion elegida: {eleccion}')
funcion_elegida = op_matematicas.get(eleccion)


resultado = operar(numero_1, numero_2, funcion_elegida)
print(
    resultado
)
