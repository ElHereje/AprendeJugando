"""
Crear un diseño de números del 1 al 100 en filas del 1 al 100.
Luego hacerlo a la inversa (del 100 al 1)
"""

# sin salto:
contador = 0
for i in range(10):
    for j in range(1, 11):
        print(f"{(i*10)+j:4}", end="")
    print()
print()

# con salto:
for i in range(0, 91, 10):
    for j in range(1, 11):
        print(f"{(i+j):4}", end="")
    print()
print()

# para hacerlo a la inversa sin salto:
for i in range(10):
    for j in range(1, 11):
        print(f"{101 - (i*10) - j:4}", end="")
    print()
print()

# a la inversa con salto:
for i in range(90, -1, 10):
    for j in range(10, 0, -1):
        print(f"{(i + j):4}", end="")
    print()
print()
