
numero_user = ''

while numero_user == '' or\
      not numero_user.isnumeric():
    numero_user = input('Ingrese un número para ver su tabla de multiplicación: ')
numero_int = int(numero_user)

for num_a in range(1, 11):
    resultado = num_a * numero_int
    print(f'{numero_int} X {num_a} = {resultado}')
