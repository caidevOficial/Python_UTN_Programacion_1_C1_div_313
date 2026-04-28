def filtrar_elementos_unicos(lista_elementos: list) -> list:
    elementos_unicos = []
    for elemento in lista_elementos:
        if elemento not in elementos_unicos:
            elementos_unicos.append(elemento)
    return elementos_unicos

def obtener_elementos_repetidos(lista_elementos_unicos: list, lista_compras_usuario: list) -> list:
    elementos_repetidos = []
    for elem_unic in lista_elementos_unicos:
        cantidad_compras = 0
        for elem_compra in lista_compras_usuario:
            if elem_unic == elem_compra:
                cantidad_compras += 1
        
        if cantidad_compras > 1:
            elementos_repetidos.append(elem_unic)
    
    return elementos_repetidos

def obtener_elementos_mas_comprados(lista_compras: list) -> list:
    
    elementos_unicos = filtrar_elementos_unicos(lista_compras)
    elementos_repetidos = obtener_elementos_repetidos(elementos_unicos, lista_compras)

    if len(elementos_repetidos) == 0:
        return lista_compras

    return elementos_repetidos

def obtener_recomendados(prod_mas_comprados: list, prod_compra_actual: list) -> list:
    recomendados = []
    for elem_mas_comp in prod_mas_comprados:
        if elem_mas_comp not in prod_compra_actual:
            recomendados.append(elem_mas_comp)
    return recomendados

def obtener_recomendaciones_de_productos(historial_compras: list, compra_actual: list) -> list:
    
    nuevo_historial_compras = historial_compras + compra_actual
    mas_comprados = obtener_elementos_mas_comprados(nuevo_historial_compras)
    recomendados = obtener_recomendados(mas_comprados, compra_actual)
    return recomendados

if __name__ == '__main__':
    historial_usuario_1 = [
        "mate", "cafe", "harina", "palmitos",
        "yerba", "mermelada", "cacao", "picadillo",
        "yerba", "yerba", "yerba", "yerba", "yerba",
        "mate", "cacao"
    ]
    compra_actual = [
        "harina", "mate", "picadillo"
    ]
    
    recomendado = obtener_recomendaciones_de_productos(historial_usuario_1, compra_actual)
    print(recomendado)