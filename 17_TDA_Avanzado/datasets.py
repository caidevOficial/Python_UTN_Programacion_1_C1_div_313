
productos = [
    #id, nombre, cantidad, precio_unit
    [1, 'Corte Pelo', 30, 15000],
    [2, 'Brushing', 10, 15000],
    [3, 'Tintura', 10, 15000],
    [4, 'Pestañas', 15, 15000],
    [5, 'Brushing Artistico', 5, 15000],
    [6, 'Maquillaje', 8, 15000]
]

clientes = [
    {
        "id": 1,
        "nombre": 'pepe'
    },
    {
        "id": 2,
        "nombre": 'moni'
    },
    {
        "id": 3,
        "nombre": 'paola'
    },
    {
        "id": 4,
        "nombre": 'maria elena'
    },
    
]

ventas = [
    {
        "id": 1,
        "id_cliente": 2
    },
    {
        "id": 2,
        "id_cliente": 1
    },
    {
        "id": 3,
        "id_cliente": 3
    }
]

detalle_ventas = [
    {
        "id": 1,
        "id_venta": 1,
        "id_producto": 1,
        "cantidad": 10
    },
    {
        "id": 2,
        "id_venta": 1,
        "id_producto": 3,
        "cantidad": 1
    },
    {
        "id": 3,
        "id_venta": 2,
        "id_producto": 2,
        "cantidad": 1
    },
    {
        "id": 4,
        "id_venta": 3,
        "id_producto": 6,
        "cantidad": 1
    }
]

# ID_V, ID_C, NOMBRE_C, MONTO_TOTAL_VENTA
