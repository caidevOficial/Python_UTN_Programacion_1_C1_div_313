datos = [
    # ID,NOMBRE,EDAD,ALTURA
    [1, 'pepe', 54, 1.7],
    [2, 'moni', 45, 1.6],
    [3, 'coqui', 16, 1.5],
    [4, 'paola', 18, 1.5],
    [4, 'maria elena', 42, 1.57]
]

for vuelta in range(2):
    
    nombre = input('Ingrese nombre: ')
    edad = int(input('Ingrese edad: '))
    altura = float(input('Ingrese altura: '))

    lista_ids_actuales = []
    for fila in datos:
        lista_ids_actuales.append(fila[0])

    set_ids_actuales = set(lista_ids_actuales)

    lista_ids_actuales = list(set_ids_actuales)

    lista_ids_actuales.reverse()
    ultimo_id_usado = lista_ids_actuales[0]
    nuevo_id_por_usar = ultimo_id_usado + 1

    nueva_persona = [nuevo_id_por_usar, nombre, edad, altura]

    datos.append(nueva_persona)

# print(lista_ids_actuales)



for persona in datos:
    print(persona)