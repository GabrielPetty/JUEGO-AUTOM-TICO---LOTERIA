
import os


def validacion():
    continuar = ""
    while continuar!= "SI" and continuar!= "NO":
        continuar = input(f'''\nDesea continuar jugando ? (si/no): ''').upper()
        if continuar!= "SI" and continuar!= "NO":
            print("Por favor, ingrese 'SI' o 'NO' para continuar...")
        elif continuar == "SI":
            return True
        elif continuar == "NO":
            os.system('cls')
            print("\n     -- * -- * --   GRACIAS POR JUGAR A LA LOTERIA AUTOMATIZADA...   -- * -- * --\n")
            return False
        else:
            print("Ingrese valores solicitados...")
   