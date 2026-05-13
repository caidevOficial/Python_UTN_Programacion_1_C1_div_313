
def mostrar_menu() -> None:
    mensaje =\
    """
    1 - Mostrar Datos: Recorrer las listas y mostrar la info con formato: 
            nombre,género,altura,peso. 
    2 - Buscar Datos: Buscar y mostrar la info completa de los 
            personajes que no superen el promedio de altura ni de peso. 
    3 - Ordenar Datos: Ordenar todas las listas por peso 
            ASC de todos los personajes. 
    4 - Filtrar Datos: Filtrar/buscar en las listas todos los 
            personajes cuyo género sea “n/a” y mostrar toda su información. 
    5 - Porcentaje de datos: Mostrar el porcentaje de personajes de cada género, 
            respecto al total de porcentajes. 
    6 - Salir. 
    """
    print(mensaje)