
import os

import Original_Juego

def Reglas():
    os.system("cls")
    print("\n")
    print("-*-"*35)
    
    print('''\n                              BIENVENIDO AL SORTEO AUTOMÁTIZADO !!!\n            
                                        REGLAMENTO:

        EL JUEGO CONSTA DE 41 NÚMEROS DESTRO DE UN BOLILLERO, LOS CUALES SE MEZCLAN.
        SE DEBE SELECCIONAR 6 NÚMEROS DEL 0 AL 40.
        LA MÁQUINA SELECCIONARÁ 12 NÚMEROS ALEATORIAMENTE.
        SI 6 DE LAS 12 BOLILLAS SACADAS COINCIDEN CON LOS 6 NÚMEROS SELECCIONADOS, USTED GANA!!!.\n
        ''')
 
    print("\n")
    print("-*-"*35)
    print(input("\n                     PRESIONE ENTER PARA INICIAR EL SORTEO..."))
  
    Original_Juego.menuPrincipal()


Reglas()