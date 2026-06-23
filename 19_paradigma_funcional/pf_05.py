

def crear_multiplicador_con_base(base: int):
    def multiplicador_con_base(numero: int) -> int:
        return base * numero
    return multiplicador_con_base


mul_base_20 = crear_multiplicador_con_base(20)
print(mul_base_20(15))

mul_base_2 = crear_multiplicador_con_base(2)
print(mul_base_2(5))
