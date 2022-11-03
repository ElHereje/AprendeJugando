# Ejemplo de la funcionalidad de "format".

# programa que calcula el precio de una cantidad de objetos de una compra


print()
print("PRESUPUESTOS".center(50))
print()

compras = [["Tornillos", 723, 23.2],
           ["Tuercas", 324, 4.5],
           ["Arandelas", 25, 35],
           ["Clavos", 1431, 2.15]]

for c in compras:
    print("{:12}: {:8} * {:8.2f}€ = {:12.2f}€".format(c[0], c[1], c[2], c[1] * c[2]))

# center --> centra el texto la cantidad entre paréntesis
# :12 --> 12 espacios
# :8.2f --> 8 espacios, con 2 decimales y float

