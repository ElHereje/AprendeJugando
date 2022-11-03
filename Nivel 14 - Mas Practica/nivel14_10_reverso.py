"""
Programa que muestre el reverso de una cadena
"""

cadena = "Hoy hace un día estupendo"
reverso = ""
for letra in cadena:
    reverso = letra + reverso
    # podemos ver como evoluciona con un print:
    print(reverso)

# otra manera podría ser con índices desde el final y
# con un salto negativo, ahorrándonos el bucle for:
# reverso = cadena[-1:-27:-1]
# esto es similar a:
# reverso = cadena[::-1]


print(reverso)  # --> odneputse aíd nu ecah yoH
