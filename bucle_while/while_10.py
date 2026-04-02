MONTO_FIJO = 7000
PRECIO_POR_MC = 200
IVA = 1.21
LIMITE_CLIENTES = 3
cant_clientes_actual = 0


# tipo_cliente = input('Ingrese su tipo de cliente [Residencial, Comercial, Industrial]: ')
# metros_consumidos_str = input('Ingrese su consumo en M3: ')
# metros_cubicos_int = int(metros_consumidos_str)

while cant_clientes_actual < LIMITE_CLIENTES:

    tipo_cliente = ''
    while tipo_cliente != 'Residencial' and\
      tipo_cliente != 'Comercial' and\
      tipo_cliente != 'Industrial':
        tipo_cliente = input('Ingrese su tipo de cliente [Residencial, Comercial, Industrial]: ')

    metros_consumidos_str = ''
    while metros_consumidos_str == '' or\
          not metros_consumidos_str.isnumeric():
        metros_consumidos_str = input('Ingrese su consumo en M3: ')
    
    metros_cubicos_int = int(metros_consumidos_str)

    cant_clientes_actual += 1

    # valor pesos
    bonificacion = 0
    recargo = 0
    bonificacion_extra = 0
    tarifa_base = (MONTO_FIJO + PRECIO_POR_MC * metros_cubicos_int)
    sub_total_2 = 0
    total_final = 0

    match tipo_cliente:
        case 'Residencial':
            if metros_cubicos_int < 30:
                bonificacion = tarifa_base * 0.1
            elif metros_cubicos_int > 80:
                recargo = tarifa_base * 0.15

            if tarifa_base < 35000:
                bonificacion_extra = tarifa_base * 0.05
                bonificacion = bonificacion + bonificacion_extra

        case 'Comercial':
            if metros_cubicos_int > 300:
                bonificacion = tarifa_base * 0.12
            elif metros_cubicos_int > 150:
                bonificacion = tarifa_base * 0.08
            elif metros_cubicos_int < 50:
                recargo = tarifa_base * 0.05
            
        case 'Industrial':
            if metros_cubicos_int > 1000:
                bonificacion = tarifa_base * 0.3
            elif metros_cubicos_int > 500:
                bonificacion = tarifa_base * 0.2
            elif metros_cubicos_int < 200:
                recargo = tarifa_base * 0.1
            
    sub_total_2 = tarifa_base - bonificacion + recargo
    total_final = sub_total_2 * IVA
    total_iva = sub_total_2 * 0.21

    mensaje =\
    f"""
    DATO USUARIO N° {cant_clientes_actual}
    Consumo Base: ${tarifa_base}
    Bonificación: ${bonificacion} 
    Recargo: ${recargo}
    ---------------
    SubTotal: ${sub_total_2}
    IVA: ${total_iva}
    _______________
    Total: ${total_final}
    """
    print(mensaje)