# Tome dos parametros: un texto y un separador (str)
# devuelva una lista de palabras

"""
"Hola mundo" -> sep: " "
["Hola", "mundo"]
"""

def agregar_si_no_vacio(lista_palabras: list[str], palabra: str) -> bool:
    hubo_cambio = False
    if palabra != '':
        lista_palabras.append(palabra)
        hubo_cambio = True
    return hubo_cambio

def split_texto(texto: str, separador: str) -> list[str]:
    lista_str = []
    palabra = ''

    for caracter in texto:
        if caracter != separador:
            palabra += caracter
        else:
            if agregar_si_no_vacio(lista_str, palabra):
                palabra = ''
    
    agregar_si_no_vacio(lista_str, palabra)
    return lista_str


texto =\
"""
pepe,54,1.70
moni,45,1.62
coqui,18,1.60
"""
# info_personas = split_texto(texto, '\n')

# for persona in info_personas:
#     datos = split_texto(persona, ',')
#     print(datos)