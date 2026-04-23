

def saludar_alumnos_utn(nombre_saludador):
    """Crea un mensaje con el texto: "Hola alumnos de la div 313" y lo devuelve

    Args:
        str: nombre_saludador: El nombre de quien esta saludando en el mensaje

    Returns:
        str: el texto como un string
    """
    mensaje = f"Hola alumnos de la div 313, los saluda: {nombre_saludador}"
    return mensaje


nombre = input('Escriba su nombre pasa saludar a la 313: ')
mensaje_print = saludar_alumnos_utn(nombre)
print(mensaje_print)