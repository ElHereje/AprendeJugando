"""
Programa que pide que tres jugadores introduzcan un número
y espera a que los tres jugadores hayan introducido el número
SI UNO QUE YA A ELEGIDO INTRODUCE DE NUEVO, EL PROGRAMA LE AVISA
"""

print("ELIGIENDO UN NÚMERO LOS JUGADORES")

jugador1 = None
jugador2 = None
jugador3 = None

while jugador1 is None or jugador2 is None or jugador3 is None:
    print()
    print("Pulsa: ")
    print("1. Para jugador A")
    print("2. Para jugador B")
    print("3. Para jugador C")
    print()
    jugador = int(input("Elige Jugador: "))
    if jugador == 1 and jugador1 is None:
        jugador1 = int(input("Dime un número: "))
    elif jugador == 1 and jugador1 is not None:
        print("El Jugador 1 ya ha elegido")
    elif jugador == 2 and jugador2 is None:
        jugador2 = int(input("Dime un número: "))
    elif jugador == 2 and jugador2 is not None:
        print("El Jugador 2 ya ha elegido")
    elif jugador == 3 and jugador3 is None:
        jugador3 = int(input("Dime un número: "))
    elif jugador == 3 and jugador3 is not None:
        print("El Jugador 3 ya ha elegido")
    else:
        print("Has elegido una opción incorrecta")

    # Otra manera
    '''jugador = int(input("Elige Jugador: "))
    if jugador == 1 and jugador1 is None:
        jugador1 = int(input("Dime un número: "))
    elif jugador == 2 and jugador2 is None:
        jugador2 = int(input("Dime un número: "))
    elif jugador == 3 and jugador3 is None:
        jugador3 = int(input("Dime un número: "))
    elif jugador in [1, 2, 3]:
        print("Este jugador ya ha elegido número.")
    else:
        print("Has introducido una opción incorrecta.")'''


else:
    print()
    print("Los tres jugadores ya han elegido número:")
    print(f" Jugador A: {jugador1}")
    print(f" Jugador B: {jugador2}")
    print(f" Jugador C: {jugador3}")


