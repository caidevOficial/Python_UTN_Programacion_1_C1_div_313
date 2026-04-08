def multiplicar(numero_a: int, numero_b: int) -> int:
    """_summary_

    Args:
        numero_a (int): _description_
        numero_b (int): _description_

    Returns:
        int: _description_
    """
    # resultado = numero_a * numero_b
    resultado = numero_b * numero_a
    return resultado

def dividir(numero_a: int, numero_b: int, mensaje_func: str = 'El resultado es: ') -> float:
    """_summary_

    Args:
        numero_a (int): _description_
        numero_b (int): _description_

    Returns:
        float: _description_
    """
    resultado = numero_a / numero_b
    mensaje_final = f'{mensaje_func} {resultado}'
    print(mensaje_final)
    # resultado = numero_b * numero_a
    return resultado

primer_num = 5
segundo_num = 10
mensaje = 'La division da de resultado: '

# resultado = dividir(primer_num, segundo_num, mensaje)
resultado = dividir(mensaje_func=mensaje, numero_b=segundo_num, numero_a=primer_num)
print(resultado)