from funciones import leer_json, escribir_json

configs = {
    "info_vendedores": [
        {
            "vendedor_actual": 'PEPE ARGENTO',
            "nivel_acceso": 'vendedor',
            "atenciones_del_dia": 7,
            "ganancias_totales_dia": 50000,
            "productos_vendidos": [
                {'nombre': 'coca', 'cantidad': 3},
                {'nombre': 'pepsi', 'cantidad': 6},
                {'nombre': '7-up', 'cantidad': 2},
                {'nombre': 'manaos', 'cantidad': 5}
            ]
        },
        {
            "vendedor_actual": 'ADMIN_VENTA_7',
            "nivel_acceso": 'administrador',
            "atenciones_del_dia": 10,
            "ganancias_totales_dia": 75000,
            "productos_vendidos": [
                {'nombre': 'coca', 'cantidad': 3},
                {'nombre': 'pepsi', 'cantidad': 6},
                {'nombre': '7-up', 'cantidad': 2},
                {'nombre': 'manaos', 'cantidad': 5}
            ]
        }
    ]
}

if __name__ == '__main__':

    escribir_json('./18_archivos/configs.json', configs)
    configs_programa = leer_json('./18_archivos/configs.json')
    
    info_vendedores = configs_programa.get('info_vendedores')
    info_usuario = info_vendedores[1]
    
    productos_vendidos = info_usuario.get('productos_vendidos')
    vendedor = info_usuario.get('vendedor_actual')
    ganancia = info_usuario.get('ganancias_totales_dia')
    atenciones = info_usuario.get('atenciones_del_dia')

    print(f'Vendedor: {vendedor}')
    print(f'                             CLIENTES ATENDIDOS: {atenciones}')
    print(f'                              Ganancias: ${ganancia}')
    print('Productos vendidos el di de hoy: ')

    for producto in productos_vendidos:
        print(f'Detalle: {producto.get("nombre")} | Cantidad: {producto.get("cantidad")}')
    
    productos_vendidos.pop()
    productos_vendidos.pop()
    productos_vendidos.pop()

    escribir_json('./18_archivos/configs.json', configs_programa)