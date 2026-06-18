from variables import ARCHIVO_TEXTO_W_1, CODIFICACION

texto = '''PEPE ARGENTO ES UN PERSONAJE
Esta es otra linea
Esta es otra linea
Esta es otra linea
Esta es otra linea
Esta es ultima linea
Esta es la ultima linea de todas
'''

archivo = open(ARCHIVO_TEXTO_W_1, 'w+', encoding=CODIFICACION)

archivo.write(texto)
archivo.seek(0)
print(archivo.read())

archivo.close()