def es_formato_entero(numero_str: str) -> bool:
    return numero_str.isnumeric()

def es_formato_floatante(numero_str: str) -> bool:
    return numero_str.count('.') == 1

def parseint_numero(numero_str: str) -> int:
    return int(numero_str)

def parsefloat_numero(numero_str: str) -> float:
    return float(numero_str)
    
def tiene_8_caracteres(texto: str) -> bool:
    return len(texto) == 8

def hacer_mayuscula(texto: str) -> str:
    return texto.upper()

def validar_input(mensaje: str,callback_val, callback_parse) -> int | float:
    numero = input(mensaje)

    if callback_val(numero):
        return callback_parse(numero)
    else:
        print('ERROR')
        return validar_input(mensaje, callback_val, callback_parse)



# resultado = validar_numero(es_formato_entero, parseint_numero)
# resultado = validar_input('ingrese un numero: ',es_formato_floatante, parsefloat_numero)
resultado = validar_input('ingrese un password: ',tiene_8_caracteres, hacer_mayuscula)
print(resultado, type(resultado))