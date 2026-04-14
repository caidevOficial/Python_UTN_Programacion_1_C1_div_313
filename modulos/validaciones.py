from variables import min_caracteres

def validar_dato_usuario(min: int, max: int) -> int:
    """Valida el input del usuario para acceder a las opciones del menú

    Args:
        min (int): la minima opcion del menu
        max (int): la maxima opcion del menu

    Returns:
        int: la opcion correcta parseada a entero
    """
    opcion = ''

    while opcion == '' or not opcion.isnumeric() or\
          (min > int(opcion) or max < int(opcion)):
        opcion = input(f'Escriba en numero entre [{min}-{max}]: ')

    return int(opcion)

def validar_numero_entero() -> int:
    opcion = ''

    while opcion == '' or not opcion.isnumeric():
        opcion = input(f'Escriba en numero entero: ')

    return int(opcion)

def validar_nombre():
    nombre = ''

    while not nombre.isalpha() or\
          len(nombre) < min_caracteres:
        nombre = input('Ingrese su nombre (minimo 3 caract.): ')
    return nombre

if __name__ == '__main__':
    cant_caracteres = len('UNIVERSIDAD')
    print(cant_caracteres)