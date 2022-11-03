"""
Programa que cree una baraja de 40 cartas, las baraja y las muestra.
Luego reparte 5 cartas a 4 jugadores. Muestra las cartas de cada
jugador, y finalmente muestre las 20 cartas restantes
"""
import random

tantos = ["A", "2", "3", "4", "5", "6", "7", "S", "C", "R"]
palos = ["oros", "copas", "espadas", "bastos"]
baraja = []

for t in tantos:
    for p in palos:
        carta = f"{t} de {p}"
        baraja.append(carta)

random.shuffle(baraja)

# todas las cartas en 4 columnas
for i in range(0, 40, 4):
    for j in range(4):
        print(f"{baraja[i+j]:13}", end=" ")
    print()
print()

# hasta aquí la 1ª parte (barajar y mostrar)
# queda repartir y mostrar

#  creamos 4 listas, una para cada jugador
jugador1 = []
jugador2 = []
jugador3 = []
jugador4 = []

# repartimos 5 cartas a cada jugador, eliminándolas de la baraja:
for i in range(5):
    carta1 = baraja.pop(0)
    jugador1.append(carta1)
    carta2 = baraja.pop(0)
    jugador2.append(carta2)
    carta3 = baraja.pop(0)
    jugador3.append(carta3)
    carta4 = baraja.pop(0)
    jugador4.append(carta4)

'''#  Una forma abreviada de repartir las cartas a los 4 jugadores:

jugadores = [ [], [], [], [] ]
for i in range(5):  # repartimos 5 cartas.....
    for j in range(4):  # ...a los 4 jugadores...
        jugadores[j].append(baraja.pop[0])'''


# mostramos las cartas de cada jugador:
jugadores = [jugador1, jugador2, jugador3, jugador4]
for i in range(4):
    print(f"Jugador {i + 1} : ")
    for j in range(5):
        print(f"{jugadores[i][j]:13}", end="")
    print()
print()

# mostramos las cartas restantes:

print("Cartas restantes en la baraja...")
print()
for i in range(0, 20, 4):  # sabemos que quedan 20 cartas
    for j in range(4):
        print(f"{baraja[i+j]:14}", end="")
    print()
