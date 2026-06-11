import funciones_generales as fg
from productos import parsear_matriz_lista

def obtener_detalle_product(productos: list[dict], producto_buscar: dict) -> dict:
    lista_info_prod = fg.filtrar_por_clave(productos, 'id', producto_buscar.get('id_producto'))
    info_prod = lista_info_prod[0]
    
    datos = {
        "id_producto": producto_buscar.get('id_producto'),
        "cantidad": producto_buscar.get('cantidad'),
        "sub_total": info_prod.get('precio_unitario') * producto_buscar.get('cantidad')
    }

    return datos

def agregar_producto_a_lista(source: list[dict], target: list[dict], busqueda: list[dict]):
    for dat_prod in source:
        datos = obtener_detalle_product(busqueda, dat_prod)
        target.append(datos)

def agregar_total_productos(info_source: dict):
    for st_prod in info_source.get('productos'):
        info_source['total'] = info_source.get('total', 0) +\
                                                st_prod.get('sub_total')
    info_source.pop('productos')

def obtener_info_cliente_venta(ventas: list[dict], clientes: list[dict], id_buscar: int) -> list[dict]:
    lista_datos_venta = fg.filtrar_por_clave(ventas, 'id', id_buscar)
    datos_venta = lista_datos_venta[0]
    datos_cliente_venta = fg.filtrar_por_clave(clientes, 'id', datos_venta.get('id_cliente'))
    return datos_cliente_venta

def crear_info_venta(id_venta: int, datos_cliente: list):
    info_venta = {
        "id_cliente": datos_cliente[0].get('id'),
        "id_venta": id_venta,
        "nombre_cliente": datos_cliente[0].get('nombre'),
        "productos": []
    }
    return info_venta

def crear_detalle_ventas_completo(datos_para_detalle: dict):
    # ID_V, ID_C, NOMBRE_C, MONTO_TOTAL_VENTA
    for id_venta in datos_para_detalle.get('ids_ventas_unicos'):

        datos_cliente_venta = obtener_info_cliente_venta(
            datos_para_detalle.get('datos_ventas'), 
            datos_para_detalle.get('datos_clientes'), id_venta)
        datos_para_detalle['dict_detalle_venta'][id_venta] = crear_info_venta(id_venta, datos_cliente_venta)
        
        lista_productos_venta = fg.filtrar_por_clave(
            datos_para_detalle.get('datos_detalle_ventas'), 'id_venta', id_venta)

        agregar_producto_a_lista(
            lista_productos_venta, 
            datos_para_detalle.get('dict_detalle_venta')[id_venta]['productos'], 
            datos_para_detalle.get('datos_productos'))

        agregar_total_productos(datos_para_detalle.get('dict_detalle_venta').get(id_venta))

def obtener_detalle_ventas_completo(datos_dv: list[dict], datos_v: list[dict], datos_c: list[dict], datos_p: list[list]):
    datos_p_lista_dict = parsear_matriz_lista(datos_p, ['id', 'nombre', 'cantidad', 'precio_unitario'])
    ids_ventas_unicos = fg.obtener_elementos_unicos(datos_dv, clave_busqueda='id_venta')
    detalles_ventas = {}

    crear_detalle_ventas_completo(
        {
            "ids_ventas_unicos": ids_ventas_unicos,
            "datos_ventas": datos_v,
            "datos_clientes": datos_c,
            "datos_detalle_ventas": datos_dv,
            "datos_productos": datos_p_lista_dict,
            "dict_detalle_venta": detalles_ventas
        }
    )

    return detalles_ventas

def obtener_detalle_venta(id_venta: int, info_venta: dict) -> str:
    id_venta = id_venta
    id_cliente = info_venta.get('id_cliente')
    nombre_cliente = info_venta.get('nombre_cliente')
    monto_venta = info_venta.get('total')
    info = f'{id_venta:04} | {id_cliente:03} | {nombre_cliente:15} | $ {monto_venta:7d}'
    return info

def mostrar_detalle_ventas(detalle_venta: dict, ordenar_por: str, modo: str = 'ASC'):
    lista_detalles_ventas = []

    for detalle in detalle_venta.values():
        lista_detalles_ventas.append(detalle)

    fg.do_selection_sort(lista_detalles_ventas, ordenar_por=ordenar_por, modo=modo)
    
    
    for detalle in lista_detalles_ventas:
        info = obtener_detalle_venta(detalle.get('id_venta'), detalle)
        print(info)



if __name__ == '__main__':
    import datasets as d_venta
    
    detalles = obtener_detalle_ventas_completo(d_venta.detalle_ventas, d_venta.ventas, d_venta.clientes, d_venta.productos)
    mostrar_detalle_ventas(detalles, ordenar_por='id_cliente', modo='DES')