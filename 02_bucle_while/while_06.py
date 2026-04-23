CLAVE_ACCESO = 123456
clave_actual = None
max_intentos = 3
intento_actual = 0
cuenta_bloqueada = False

while clave_actual != CLAVE_ACCESO and intento_actual < max_intentos:
    clave_actual = int(input('Ingrese su clave de 6 digitos: '))

    if clave_actual != CLAVE_ACCESO:
        print('Su clave es incorrecta.')
    intento_actual += 1

    if intento_actual == max_intentos:
        print('Su cuenta fue bloqueada')
        cuenta_bloqueada = True

if not cuenta_bloqueada:
    print('🐦‍🔥 Bienvenido al sistema!')
else:
    print('⚠️ Contacte a soporte xq su cuenta fue bloqueada')
