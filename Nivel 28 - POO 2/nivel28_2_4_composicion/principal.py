from hipodromo import Hipodromo
import os, time


def portada():
    print("  ------------------------------------------")
    print("           BIENVENIDO A LAS CARRERAS")
    print("  ------------------------------------------")
    print()
    print("             Elige un hipódromo")
    print()
    print("     1. Hipódromo de La plata")
    print("     2. Hipódromo de Santiago")
    print("     3. Hipódromo de La Zarzuela")
    print()
    opcion = ""
    while opcion not in ("1", "2", "3"):
        opcion = input("    --> ")
    return opcion

def mostrar_gandores(ganadores):
    print()
    print("     Ganadores: ", end=" ")
    for caballo in ganadores:
        print(caballo, end=" ")
    print()
    print()



################ FLUJO DEL PROGRAMA ###############

os.system("cls")
opcion = portada()

if opcion == "1":
    hipodromo = Hipodromo("LA PLATA", 8, 40, "-")
elif opcion == "2":
    hipodromo = Hipodromo("SANTIAGO", 10, 45, ".")
elif opcion == "3":
    hipodromo = Hipodromo("LA ZARZUELA", 6, 50, "_")


    
os.system("cls")
hipodromo.poner_caballos()
hipodromo.mostrar()
hipodromo.mostrar_favoritos()
input(" Elige caballo y pulsa 'Enter'...")

# Bucle ppal
while True:
    
    os.system("cls")
    ganadores = hipodromo.comprobar_ganadores()
    if len(ganadores) > 0:
        break

    hipodromo.poner_ornamento()
    hipodromo.avanzar_caballos()
    hipodromo.poner_caballos()
    hipodromo.mostrar()

    time.sleep(1)

hipodromo.mostrar()
mostrar_gandores(ganadores)
