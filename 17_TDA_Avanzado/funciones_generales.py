
def filtrar_por_clave(datos: list[dict], clave: str, valor: int) -> list[dict]:
    filtrados = []

    for dato in datos:
        if dato.get(clave) == valor:
            filtrados.append(dato)
    return filtrados

def obtener_elementos_unicos(datos: list[dict], clave_busqueda: str) -> list:
    unicos = set()

    for dato in datos:
        unicos.add(dato.get(clave_busqueda))
    
    unicos = list(unicos)
    unicos.sort()

    return unicos

def do_selection_sort(elementos: list[dict], ordenar_por: str, modo : str = 'ASC'):

    tamanio_lista = len(elementos)

    for indice_a in range(tamanio_lista - 1):

        indice_menor = indice_a

        for indice_b in range(indice_a + 1, tamanio_lista):
            
            diccionario_im = elementos[indice_menor]
            diccionario_ib = elementos[indice_b]

            if diccionario_im.get(ordenar_por) > diccionario_ib.get(ordenar_por) and modo == 'ASC' or\
               diccionario_im.get(ordenar_por) < diccionario_ib.get(ordenar_por) and modo == 'DES':
                indice_menor = indice_b
        
        if indice_menor != indice_a:
            elementos[indice_menor], elementos[indice_a] =\
            elementos[indice_a], elementos[indice_menor]