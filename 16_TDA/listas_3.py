from listas_2 import split_texto

info_persona = ['pepe', '54', '1.70']
# pepe,54,1.70

def join_lista_a_texto(lista_palabras: list[str], separador: str) -> str:
    texto_nuevo = ''
    for elemento in lista_palabras:
        texto_nuevo += f'{elemento}{separador}'

    texto_nuevo = texto_nuevo[:-1]

    return texto_nuevo

# print(info_persona)

# lista_a_texto = join_lista_a_texto(info_persona, ',')
# texto_a_lista = split_texto(lista_a_texto, ',')


# print(
#     lista_a_texto,
#     texto_a_lista
# )