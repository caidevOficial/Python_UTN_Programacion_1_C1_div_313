from utn_fra_datasets.datasets import (
    lista_poke_nombres, lista_poke_ids,
    lista_poke_poderes, lista_poke_tipos,
    lista_poke_condiciones
)

def trasponer_matriz(matriz: list[list]) -> list[list]:
    matriz_t = []

    cant_col = len(matriz[0])
    cant_fil = len(matriz)

    for indice_col in range(cant_col):

        nueva_fila = []

        for indice_fila in range(cant_fil):
            elemento = matriz[indice_fila][indice_col]
            nueva_fila.append(elemento)

        matriz_t.append(nueva_fila)
    
    return matriz_t

def es_numero_valido(numero: str):
    return numero.isnumeric()

def pedir_numero(tipo_num: str):
    numero = input(f'Escribe un numero de {tipo_num}: ')
    if not es_numero_valido(numero):
        print(f'ERROR! {numero} no es un numero valido')
        return pedir_numero(tipo_num)
    return int(numero)

def es_numero_valido_v2(numero: str, nums_existentes: list[int]):
    return numero.isnumeric() and int(numero) in nums_existentes

def pedir_numero_v2(tipo_num: str, nums_existentes: list[int]):
    numero = input(f'Escribe un numero de {tipo_num}: ')
    if not es_numero_valido_v2(numero, nums_existentes):
        print(f'ERROR! {numero} no es un numero valido')
        return pedir_numero_v2(tipo_num, nums_existentes)
    return int(numero)

def es_dato_valido(tipo_dato: str, dato: str):
    # validar que sea alpha
    if tipo_dato == 'condicion' and dato in ['legendario', 'normal']:
        return True
    if tipo_dato != 'condicion' and dato.isalpha():
        return True
    else:
        return False

def pedir_dato(tipo_dato: str):
    condiciones = '[normal o legendario]'
    if tipo_dato != 'condicion':
        condiciones = ''

    dato = input(f'ingrese un {tipo_dato} {condiciones}:')
    if not es_dato_valido(tipo_dato, dato):
        print(f'ERROR! el dato {dato} no es valido.')
        return pedir_dato(tipo_dato)
    return dato

def cargar_dato(num_vuelta: int):
    match num_vuelta:
        case 0:
            return pedir_numero('ID')
        case 1:
            return pedir_dato('nombre')
        case 2:
            return pedir_dato('tipo')
        case 3:
            return pedir_numero('poder')
        case 4:
            return pedir_dato('condicion')

def modificar_dato_pokemon(pokemon: list):
    print('POKEMON SELECCIONADO:')
    print(pokemon)
    modificacion = input('Que dato quiere modificar? [id,nombre,tipo,poder,condicion]: ')

    match modificacion:
        case 'id':
            nuevo_id = pedir_numero('ID')
            pokemon[0] = nuevo_id
        case 'nombre':
            nuevo_nombre = pedir_dato('nombre')
            pokemon[1] = nuevo_nombre
        case 'tipo':
            nuevo_tipo = pedir_dato('tipo')
            pokemon[2] = nuevo_tipo
        case 'poder':
            nuevo_poder = pedir_numero('poder')
            pokemon[3] = nuevo_poder
        case 'condicion':
            nueva_condicion = pedir_dato('condicion')
            pokemon[4] = nueva_condicion
    print('Registro Pokemon modificado exitosamente')
    print(pokemon)
        
        

def actualizar_matriz(matriz_source: list[list], matriz_dest: list[list]):

    for indice_fila in range(len(matriz_source)):

        dato = matriz_source[indice_fila][1]
        matriz_dest[indice_fila].append(dato)

def mostrar_datos_matriz_fc(matriz: list[list]):

    cant_col = len(matriz[0])
    cant_fil = len(matriz)

    for fila in range(cant_fil):

        info = ''

        for col in range(cant_col):
            info += f'{matriz[fila][col]},'
        
        info = info[0:-1]
        print(info)

def obtener_ids(matriz_poke: list[list]) -> list[int]:
    lista_ids = []
    for fila in matriz_poke:
        lista_ids.append(fila[0])
    return lista_ids

def buscar_pokemon_por_dato(matriz_poke: list[list], columna_dato: int, valor: int) -> list:
    pokemon_buscado = []
    for pokemon in matriz_poke:
        if pokemon[columna_dato] == valor:
            pokemon_buscado = pokemon
    return pokemon_buscado

def borrar_pokemon_por_id(matriz_poke: list[list], id_a_borrar: int):
    indice_id = 0
    for indice_poke in range(len(matriz_poke)):
        if matriz_poke[indice_poke][0] == id_a_borrar:
            indice_id = indice_poke
            break
    print(f'Pokemon a borrar: {matriz_poke[indice_id]}')
    borrar = input('Seguro que desea borrar? [s/n]: ')
    if borrar == 's':
        matriz_poke.pop(indice_id)
        print(f'Pokemon borrado exitosamente')
    else:
        print('Operacion cancelada')

def modificar_datos(matriz_poke: list[list]):
    print('## MENU MODIFICACION DE POKEMON ##')
    mostrar_datos_matriz_fc(matriz_poke)
    lista_ids = obtener_ids(matriz_poke)
    id_seleccionado = pedir_numero_v2('ID', lista_ids)
    poke_seleccionado = buscar_pokemon_por_dato(matriz_poke, 0, id_seleccionado)
    modificar_dato_pokemon(poke_seleccionado)

def borrar_dato(matriz_poke: list[list]):
    print('## MENU BORRADO DE POKEMON ##')
    mostrar_datos_matriz_fc(matriz_poke)
    lista_ids = obtener_ids(matriz_poke)
    id_seleccionado = pedir_numero_v2('ID', lista_ids)

    borrar_pokemon_por_id(matriz_poke, id_seleccionado)
    
    



def cargar_datos_pokemon(matriz_poke: list[list]):

    datos_validados_m = [
        ['id'],
        ['nombre'],
        ['tipo'],
        ['poder'],
        ['condicion']
    ]

    # Matriz version base
    for vuelta in range(5):
        dato = cargar_dato(vuelta)
        # datos_validados.append(dato)
        datos_validados_m[vuelta].append(dato)

    # # matriz version T
    # datos_validados = []
    # for vuelta in range(5):
    #     dato = cargar_dato(vuelta)
    #     datos_validados.append(dato)
    # datos_validados = [4,charmander,fuego,5,normal]
    # matriz_poke.append(datos_validados)
    
    # print(datos_validados)
    print(datos_validados_m)

    actualizar_matriz(datos_validados_m, matriz_poke)
    print()
    print(matriz_poke)




if __name__ == '__main__':
    matriz_poke = [
        lista_poke_ids, lista_poke_nombres, 
        lista_poke_tipos, lista_poke_poderes, 
        lista_poke_condiciones
    ]

    # 004,charmander,fuego,5,normal
    
    """
    matriz_pokemons_t = [
        [244,'entei','fuego',30,'legendario'],
        [28,'sandslash','suelo',15,'normal'],
        [584,'vanilluxe','hielo',15,'normal'],
        [26,'raichu','eléctrico',20,'normal'],
        [9,'blastoise','agua',18,'normal']
    ]
    """

    cargar_datos_pokemon(matriz_poke)
    poke_t = trasponer_matriz(matriz_poke)
    modificar_datos(poke_t)
    
    for i in range(3):
        borrar_dato(poke_t)
    
    
    matriz_poke = trasponer_matriz(poke_t)
    print(matriz_poke)
    
    

    # print()
    # mostrar_datos_matriz_fc(poke_t)

