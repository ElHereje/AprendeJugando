"""
Igual pero mostrarlos con 2 for anidados
"""


tantos = ["A", "2", "3", "4", "5", "6", "7", "S", "C", "R"]
palos = ["Oros", "Copas", "Espadas", "Bastos"]
baraja = []

for tanto in tantos:
    for palo in palos:
        # print(f"{tanto} de {palo}")
        baraja.append(f"{tanto} de {palo}")

for i in range(0, 40, 4):
    for j in range(4):
        print(f"{baraja[i + j]:16}", end="")
    print()



