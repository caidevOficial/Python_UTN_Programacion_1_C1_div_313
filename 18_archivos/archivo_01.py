from variables import ARCHIVO_TEXTO_1, ARCHIVO_TEXTO_W_1

mi_archivo = open(ARCHIVO_TEXTO_W_1, 'r', encoding='UTF-8')
contenido = mi_archivo.read()
mi_archivo.close()

print(contenido)