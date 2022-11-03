"""
crea una baraja añadiendo las cartas con bucles for
"""

tantos = ["A", "2", "3", "4", "5", "6", "7", "S", "C", "R"]
palos = ["Oros", "Copas", "Espadas", "Bastos"]
baraja = []

for tanto in tantos:
    for palo in palos:
        print(f"{tanto} de {palo}")
        baraja.append(f"{tanto} de {palo}")

print(baraja)

# para mostrarlos en orden podemos poner
for i in range(0, 40, 4):  # del primero al último de 4 en 4
    print(f"{baraja[i]} {baraja[i+1]} {baraja[i+2]} {baraja[i+3]}")



