## JUEGO DE LOTERÍA CON ACIERTO DE 6 NÚMEROS, AUTOMÁTICA.

from ast import Break
import numbers
from random import*
import os
from unittest import result

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
    #print('''\n             
    #    1 : Seleccione la cantidad de Jugadores a participar
    #    2 : Debe ingresar 6 números del 0 al 40 para comenzar el
    #        sorteo, los números se ingresan de a uno a la vez.\n''')  
    print("\n")
    print("-*-"*35)
    print(input("\n                     PRESIONE ENTER PARA INICIAR EL SORTEO..."))
  
    menuPrincipal()

def menuPrincipal():
    os.system('cls')
    listaNum = []
    for cuenta in range(41):
        listaNum.append(cuenta)
  
    def validoLoteria():
        bingo = []
        
        def numeroReal():
            numero = 0
            sel = 1
            valido = True
            while sel <= 6:
                try:
                    while numero== 0 or numero<=40:
                        numero == True
                        if numero== 0 or numero<=40:
                            if sel <=6:
                                print("\n                                                  LISTA DE NÚMEROS DEL SORTEO\n", "\n",listaNum)
                                numero = int(input('\nSELECCIONE NÚMERO Y PRESIONE "ENTER": '))
                                os.system("cls")
                                if numero not in bingo:
                                    
                                    bingo.append(numero)
                                    sel+=1
                                else:
                                    print(" _ "*35)
                                    print("\n            NÚMERO YA SELECCIONADO !!! ELIJA OTRO.")
                            else:
                                break
                    else:
                        os.system("cls")
                        print("\n                                         LOS NÚMEROS HA INGRESAR DEBEN SER DEL 0 al 40\n")
                        print("-_-_-"*30)
                        print("\n                                                ELIJA LOS 6 NÚMEROS NUEVAMENTE...\n")
                        #print("LISTA DE NÚMEROS PARA SELECCIONAR\n", listaNum)
                        bingo.clear()
                        numeroReal()
                    break
                except ValueError:
                    print("\n        INGRESE VALORES ENTEROS, ejemplo 2 - 5 - 10...")

        numeroReal()
        os.system("cls")
        print("\nComienza el juego...")
        print('''
                   SE MEZCLARÁN LAS BOLILLAS Y SE INGRESARÁN 12 NÚMEROS ALEATORIOS, 
                                             "SUERTE!!!"...''')
        print(input("\nCOMENCEMOS...PRESIONE ENTER."))
        numBolillas = []
        numBolillas = sample(listaNum,12)
        os.system('cls')    
        bingo.sort()
        numBolillas.sort()

        print("-*-"*50)
        
        print("\n               DEBE ACERTAR LOS 6 NÚMEROS SELECCIONADOS !!!\n")
        print("Números Seleccionados: \n", ' - '.join(map(str, bingo)))## EN CASO DE QUERER VER LOS VALORES SELECCIONADOS.
        print("\nNúmeros ganadores: \n", ' - '.join(map(str, numBolillas)), '\n')## EN CASO DE QUERER VER LOS VALORES GANADORES.
    
        print('\n', '-'*35, '\n')
    
        numBolillas.extend(bingo)
        numBolillas.sort()

        while len(numBolillas) >0:
            ganador = []
            resultado = []
            if len(numBolillas) >0:
                for numero in numBolillas:
                    if numero not in resultado:
                        resultado.append(numero)
                        if len(resultado) == 18:
                            print("No hubo aciertos..., ""\nINTENTE NUEVAMENTE !!!")
                            break
                    else:
                        ganador.append(numero)
                for numeros in ganador:
                    if len(ganador) ==6:
                        print("\nHA GANADOOOO !!! FELICIDADES...")
                        print("SUS NÚMEROS GANADORES SON: \n", ' - '.join(map(str, ganador)))
                        break
                    else:
                        ganadorT = len(ganador)
                        print("\nUsted acertó: ", ganadorT, "número/s.")
                        print("\n     ", ' - '.join(map(str, ganador)), "\n", "\nINTENTE NUEVAMENTE !!!\n")
                        break
                break

        def validacion():
            continuar = ""
            while continuar!= "SI" and continuar!= "NO":
                continuar = input(f'''\nDesea continuar jugando ? (si/no): ''').upper()
                if continuar!= "SI" and continuar!= "NO":
                    print("Por favor, ingrese 'SI' o 'NO' para continuar...")
                elif continuar == "SI":
                    menuPrincipal()
                elif continuar == "NO":
                    os.system('cls')
                    print("\n     -- * -- * --   GRACIAS POR JUGAR A LA LOTERIA AUTOMATIZADA...   -- * -- * --\n")
                else:
                    print("Ingrese valores solicitados...")
        validacion()    
    validoLoteria()

Reglas()
