
def validar_edad(edad_min: int, edad_max: int) -> int:
    edad_str = input('Ingrese su edad: ')
    edad_int = None

    if not edad_str.isnumeric() or\
       not (edad_min <= int(edad_str) <= edad_max):
        print('ERROR. Edad inválida.')
        edad_int = validar_edad(edad_min, edad_max)
    
    if edad_int != None:
        return edad_int
    else:
        return int(edad_str)


if __name__ == '__main__':
    edad = validar_edad(18, 60)
    print(f'Edad valida es: {edad}')