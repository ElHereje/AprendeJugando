'''
Simulación de movimiento con bucle
'''

import os
import time

espacios = " "

for i in range(20):
    time.sleep(0.3)
    os.system("cls")

    print(f"{espacios}  O ")
    print(f"{espacios} /|\ ")
    print(f"{espacios} / | ")

    espacios += " "

    time.sleep(0.3)
    os.system("cls")

    print(f"{espacios}  O  ")
    print(f"{espacios} /|) ")
    print(f"{espacios} | | ")

    espacios += " "

    time.sleep(0.3)
    os.system("cls")

    print(f"{espacios}  O  ")
    print(f"{espacios} (|\ ")
    print(f"{espacios} | | ")

    espacios += " "

    time.sleep(0.3)
    os.system("cls")

    print(f"{espacios}  O  ")
    print(f"{espacios} /|\ ")
    print(f"{espacios} | \ ")

    espacios += " "