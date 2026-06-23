
def crear_operacion_matematica():
    """
    Se encarga de crear una funcion entre sum, res, mult, div
    """
    operacion = input('Que operacion queres hacer? [div,mul,sum,res]: ')

    def suma(num1, num2):
        """_summary_
        Suma dos numeros
        Args:
            num1 (_type_): _description_
            num2 (_type_): _description_

        Returns:
            _type_: _description_
        """
        return num1 + num2
    
    def mult(num1, num2):
        return num1 * num2
    
    def divi(num1, num2):
        return num1 / num2
    
    def rest(num1, num2):
        return num1 - num2
    
    match operacion:
        case 'mul':
            print('Eleccion: MULTIPLICACION')
            return mult
        case 'div':
            print('Eleccion: DIVISION')
            return divi
        case 'sum':
            print('Eleccion: SUMA')
            return suma
        case 'res':
            print('Eleccion: RESTA')
            return rest
        

mi_operacion = crear_operacion_matematica()
numero_1 = 20
numero_2 = 100
    
print(
    mi_operacion(numero_1, numero_2)
)