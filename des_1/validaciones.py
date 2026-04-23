
def es_string_numerico_valido(num_str: str) -> bool:
    # -1000
    indice_guion = None
    cantidad_actual_guion = 0
    guion_indice_correcto = False
    resto_elementos_num = True

    for indice_carac in range(len(num_str)):
        if num_str[indice_carac] == '-':
            indice_guion = indice_carac
            cantidad_actual_guion += 1
    
    ##########################################
    if indice_guion == None:
        indice_comienzo_validacion = 0
    elif indice_guion == 0:
        indice_comienzo_validacion = 1
        guion_indice_correcto = True
    else:
        return False
    
    for indice_carac in range(indice_comienzo_validacion, len(num_str)):
        if not num_str[indice_carac].isnumeric():
            resto_elementos_num = False
            break
    
    positivo_valido = resto_elementos_num and indice_guion == None
    negativo_valido = resto_elementos_num and guion_indice_correcto
    
    return positivo_valido or negativo_valido

def es_entero(num):
    pass

def validar_numero_input():
    numero_str = input('Ingrese un numero entre -1000 y 1000: ')

    if not es_string_numerico_valido(numero_str) or not (-1000 <= float(numero_str) <= 1000):
        print('Error, numero incorrecto')
        numero_str = validar_numero_input()
    
    if type(numero_str) == str and es_entero(numero_str):
        return int(numero_str)
    elif type(numero_str) == str and not es_entero(numero_str):
        return float(numero_str)
    else:
        return numero_str

if __name__ == '__main__':
    
    print(validar_numero_input())