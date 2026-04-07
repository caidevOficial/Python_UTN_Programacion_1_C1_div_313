"""
Realizar un programa que permita mostrar una pirámide de números. 
Por ejemplo: si se ingresa el numero 5, 
la salida del programa será la siguiente:
1
12
123
1234
12345
"""

user_input = int(input('Ingrese un número: '))
siguiente_user_input = user_input + 1

for num_a in range(1, siguiente_user_input):
    for num_b in range(1, num_a + 1):
        print(num_b, end='')
        # 
    print()

mensaje = ''
for num_c in range(1, siguiente_user_input):
    # mensaje = f'{mensaje}{num_c}'
    mensaje += str(num_c)
    print(mensaje)