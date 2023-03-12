'''
Programa que pida que adivines un nº del 1 L 10
añade un contador que indique los intentos
necesarios
'''

import random

numero = random.randint(0,10)
prueba = int(input("Adivina un nº del 1 al 10: "))
contador = 1
print(f"...secreto...el nº es el {numero}....")

while numero != prueba:
    prueba = int(input("ERROR..Pruebas otra vez: "))
    contador += 1
else:
    print(f"Correcto. El nº era el {numero}")
    print(f"Has tenido {contador} fallos...")
