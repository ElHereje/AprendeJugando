from caballo import Caballo
from hipodromo import Hipodromo
import time
import random
import os


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


################ FLUJO DEL PROGRAMA ###############

os.system("cls")
opcion = portada()

if opcion == "1":
    hipodromo = Hipodromo("LA PLATA", 8, 40, "-")
elif opcion == "2":
    hipodromo = Hipodromo("SANTIAGO", 10, 45, ".")
elif opcion == "3":
    hipodromo = Hipodromo("LA ZARZUELA", 6, 50, "_")
    
# ahora creamos los caballos para poder agragarlos
nombres = ["r", "s", "t", "p", "n", "k", "w", "y", "f", "z"] # 10 nombres
caballos = []
for i in range(hipodromo.filas): # elegimos favorito o no..
    favorito = random.choice([True, False])
    caballo = Caballo(nombres[i], favorito)
    caballos.append(caballo) # lo agragamos a la lista
    
# agregamos los caballos creados al hipodromo
for i in range(hipodromo.filas):
    hipodromo.poner_caballo(caballos[i], i, caballos[i].metro) # objeto caballo, i, metro
    
    
os.system("cls")

hipodromo.mostrar()

print()
print(" Los caballos favoritos de hoy son: ", end=" ")
for caballo in caballos:
    print(caballo, end=" ")
print()
input(" Elige caballo y pulsa 'Enter'...")


# Bucle ppal
while True:
    
    os.system("cls")
    caballos_ganadores = []
    for caballo in caballos:
        # cuando llega un caballo a la meta
        if caballo.metro > hipodromo.metros - 7: # restamos un nº para que no se salga de indice
            caballos_ganadores.append(caballo)
    if len(caballos_ganadores) > 0: # si algun caballos a llegado a la meta
        break  # acabamos cuando hay un ganador
    
     # si no es así, seguimos iterando por el bucle ppal...
    
    # al ir avanzando, vamos cambiando el nombre del caballos por el ornamento
    for i in range(hipodromo.filas):
        hipodromo.poner_caballo(hipodromo.ornamento, i, caballos[i].metro)
        
    # vamos haciendo avanzar los caballos con el nuevo metro
    for i in range(hipodromo.filas):
        caballos[i].avanzar()
        hipodromo.poner_caballo(caballos[i], i, caballos[i].metro)
        
    hipodromo.mostrar()
    
    time.sleep(1) # esperamos un segundo antes de volver al ppio bucle
    
hipodromo.mostrar()
print()
print(" Ganadores: ", end=" ")
for caballo in caballos_ganadores:
    print(caballo, end=" ")
print()