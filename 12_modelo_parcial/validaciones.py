
def validar_input(min: str, max: str) -> str:

    input_usr = input(f'Ingrese una opcion entre: [{min}-{max}]: ')
    if input_usr < min or input_usr > max:
        print(f'Error, ingrese un numero entre [{min}-{max}]: ')
        input_usr = validar_input(min, max)
    
    return input_usr

if __name__ == '__main__':
    print(validar_input('1', '4'))