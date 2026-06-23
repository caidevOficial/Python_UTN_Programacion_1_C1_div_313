
def sumar_5_al_numero(numero: int) -> int:
    return numero + 5


def creadora_de_funciones():
    return sumar_5_al_numero


sumar_5 = creadora_de_funciones()

print(sumar_5(10))