from variables import ARCHIVO_TEXTO_W_1
texto = 'murcielago 120'

lista_texto = [
    "Esta es una linea\n",
    "Esta es otra linea\n",
    "Esta es otra linea\n",
    "Esta es otra linea\n",
    "Esta es otra linea\n",
    "Esta es ultima linea\n"
]

archivo = open(ARCHIVO_TEXTO_W_1, 'w', encoding='utf-8')

# print(archivo.write(texto))
print()
archivo.writelines(lista_texto)
archivo.close()