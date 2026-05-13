
def validar_input(min: str, max: str) -> str:
    input_usr = input(f'Ingrese una opción entre [{min} - {max}]: ')

    if not (min <= input_usr <= max):
        print('ERROR. Opción inválida.')
        input_usr = validar_input(min, max)
    
    return input_usr
