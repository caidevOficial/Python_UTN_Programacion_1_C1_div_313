# MAIN
from dataset import ( 
    lista_sw_nombres, 
   lista_sw_generos, 
   lista_sw_alturas, 
   lista_sw_pesos
)
from app import applicacion

# from app import aplicacion
if __name__ == '__main__':
    applicacion(lista_sw_nombres, lista_sw_generos, lista_sw_alturas, lista_sw_pesos)