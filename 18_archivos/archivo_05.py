from variables import ARCHIVO_TEXTO_W_1, CODIFICACION

texto = 'ESTO ES UNA  INFORMACIÓN EXTRA!\n'

archivo = open(ARCHIVO_TEXTO_W_1, 'a+', encoding=CODIFICACION)

archivo.write(texto)
archivo.seek(0)
print(archivo.read())

archivo.close()