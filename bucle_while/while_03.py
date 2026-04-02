encuestados = 0
cant_f1 = 0
cant_futbol = 0
limite_encuestas = 5

while encuestados < limite_encuestas:

    dato_actual = encuestados + 1

    respuesta = input(f'Dato N°{dato_actual} ->  1 - Formula | 2 - Futbol: ')
    respuesta_int = int(respuesta)

    match respuesta_int:
        case 1:
            cant_f1 += 1
        case 2:
            cant_futbol += 1
    
    encuestados += 1

porcent_f1 = (cant_f1 * 100) / encuestados
porcent_futbol = (cant_futbol * 100) /encuestados

mensaje =\
f'''
Encuestados: {encuestados}
F1 %: {porcent_f1}
Futbol %: {porcent_futbol}
'''    
print(mensaje)