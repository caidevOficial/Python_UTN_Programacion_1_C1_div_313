def calcular_precio_con_iva(precio_base: float, iva: int = 21) -> float:
    """Le agrega el IVA al precio base de un producto

    Args:
        precio_base (int, float): el precio base del producto sin el iva
        iva (int, optional): Impueto nacional el cual puede ser 21 o 10,5. Defaults to 21.

    Returns:
        float: Devuelve el precio del producto con el IVA agregado (sea 21 o 10,5)
    """
    mult_iva = (iva / 100 + 1)
    precio_con_iva = precio_base * mult_iva
    return precio_con_iva

precio_base = float(input('Ingrese precio base: '))
precio_iva_completo = calcular_precio_con_iva(precio_base, iva=21)
precio_medio_iva = calcular_precio_con_iva(precio_base, iva=10.5)
print(precio_iva_completo, precio_medio_iva)
