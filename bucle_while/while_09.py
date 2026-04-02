"""
tipo_cliente = input('Ingrese su tipo de cliente [Residencial, Comercial, Industrial]: ')
"""

tipo_cliente = ''

while tipo_cliente != 'Residencial' and\
      tipo_cliente != 'Comercial' and\
      tipo_cliente != 'Industrial':
    tipo_cliente = input('Ingrese su tipo de cliente [Residencial, Comercial, Industrial]: ')

print(f'Su tipo de cliente es: {tipo_cliente}')    