from variables import ARCHIVO_TEXTO_W_1, CODIFICACION


with open(ARCHIVO_TEXTO_W_1, 'r', encoding=CODIFICACION) as archivo:
    contenido = archivo.read()

print(contenido)