"""
Programa que permita convertir unidades de masa:
Kilogramos a libras y libras a kilogramos.
1 kg = 2.20462262 lbs --> 1 lb = 1 / 2.20462262 kg
"""


def pasa_a_kilo(libras):
    return libras / 2.20462262


def pasa_a_libra(kilos):
    return kilos * 2.20462262


def menu():
    print()
    print("Introduce Opción (1-3): ")
    print("1. Pasar a Kilos.")
    print("2. Pasar a Libras.")
    opc = input("--> ")
    return opc


opcion = menu()

if opcion == 1:
   libras = int(input("Introduce cantidad de Libras: "))
   resultado = pasa_a_kilo(libras)
   print(f"{libras} lbs son {resultado} Kg")
elif opcion == 2:
    kilos = int(input("Introduce cantidad de Kilos: "))
    resultado = pasa_a_libra(kilos)
    print(f"{kilos} kg son {resultado} lbs")


