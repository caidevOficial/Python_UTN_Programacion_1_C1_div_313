from variables import ARCHIVO_TEXTO_W_1, CODIFICACION


archivo = open(ARCHIVO_TEXTO_W_1, 'r+', encoding=CODIFICACION)


contenido = archivo.read()
archivo.write('Esta es la ultima linea de todas\n')
archivo.seek(0)
contenido = archivo.read()

print(contenido)

archivo.close()