
"""
Tener un diccionario donde cada clave sea una letra y cada valor sea
la cantidad de veces que aparece esa letra

ej:

{
    "B": 1,
    "i": 8
}
"""
from listas_2 import split_texto
texto = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since 1966, when designers at Letraset and James Mosley, the librarian at St Bride Printing Library, took a 1914 Cicero translation and scrambled it to make dummy text for Letraset's Body Type sheets. It has survived not only many decades, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised thanks to these sheets and more recently with desktop publishing software including versions of Lorem Ipsum."""


def contar_palabras(texto: str) -> dict:
    diccionario_cuentas = {}
    for palabra in split_texto(texto, ' '):
        if palabra not in diccionario_cuentas.keys():
            diccionario_cuentas[palabra] = 1
        else:
            diccionario_cuentas[palabra] += 1
    return diccionario_cuentas

def contar_palabras_v2(texto: str) -> dict:
    cantidades = {}
    for palabra in split_texto(texto, ' '):
        cantidades[palabra] = cantidades.get(palabra, 0) + 1
    return cantidades

if __name__ == '__main__':
    
    diccionario_palabras = contar_palabras_v2(texto)
    for clave,valor in diccionario_palabras.items():
        print(f'{clave} : {valor}')