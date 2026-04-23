# import validaciones as val
from validaciones import validar_numero_entero

def es_par(numero: int) -> bool:
    """
    Se encarga de validar de que el número de viene por parametro
    sea un número par o impar.

    Args:
        numero (int): El nú,ero el cual hay que verificar si es par o impar.
    
    Returns:
            Retorna True si el número es par, Falso caso contrario.
    """
    es_par = False
    if numero % 2 == 0:
        es_par = True
    return es_par

def verificar_numero_par():
    condicion_par = ''
    numero = validar_numero_entero()
    num_par = es_par(numero)
    if not num_par:
        condicion_par = 'NO '
    mensaje = f'El numero {numero} {condicion_par}es PAR'
    print(mensaje)
    return None

def buscar_divisor(numero: int, min_rango: int, max_rango: int) -> bool:
    no_hay_divisor = True
    for num in range(min_rango, max_rango):
        if numero % num == 0:
            no_hay_divisor = False
            break
    return no_hay_divisor

def es_primo(numero: int) -> bool:
    if numero < 2:
        cond_primo = False
    elif numero == 2:
        cond_primo = True
    else:
        # Tenemos en cuenta que ya tiene dos divisores
        # el 1 y el mismo numero, con encontrar otro
        # que no sean los mencionados, el numero NO es primo
        cond_primo = buscar_divisor(numero=numero, min_rango=2, max_rango=numero)

    return cond_primo


def verificar_si_es_primo() -> None:
    condicion_primo = ''
    numero = validar_numero_entero()
    num_primo = es_primo(numero)
    if not num_primo:
        condicion_primo = 'NO '
    mensaje = f'El numero {numero} {condicion_primo}es PRIMO'
    print(mensaje)
    return None
