# BANDERA O BREAK

"""
Programa que pide letras hasta que la adivines. Entonces se para.
Se puede probar con todas menos con la "w", en cuyo caso indica que no está
permitida y se para el programa.
"""

letra = "a"
while True:
    intento = input("Dime una letra(menos la w): ")
    if intento == letra:
        print(f"Acertastes. La letra era la {intento}.")
        break
    elif intento == "w":
        print("Letra prohibida. Fin del juego.")
        break
    else:
        print("Incorrecto. inténtalo de nuevo...")
print("Fin del programa")
