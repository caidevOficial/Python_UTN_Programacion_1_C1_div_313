## MCM
# MCD

def obtener_maximo_comun_divisor(numero_a: int, numero_b: int) -> int:
    if numero_b == 0:
        return numero_a
    else:
        modulo_a_b = numero_a % numero_b
        resultado = obtener_maximo_comun_divisor(numero_b, modulo_a_b)
        return resultado

if __name__ == '__main__':
    ma_co_di = obtener_maximo_comun_divisor(16, 32)
    print(f'El MCD entre 10 y 5 es: {ma_co_di}')