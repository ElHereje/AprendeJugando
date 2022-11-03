"""
En una tienda quieren hacer inventario de las figuras
que tienen y el número de unidades de cada una.
Crea una lista que contenga los datos del inventario:
    * 6 cuadrados
    * 5 círculos
    * 4 triángulos
    * 3 rectángulos
"""
figuras = [["Cuadrados", 6],
           ["Círculos", 5],
           ["Triángulos", 4],
           ["Rectángulos", 3]]

# Imaginemos que la tienda tiene una estantería con 4 columnas y 3 filas,
# y queremos saber donde se sitúa cada uno de los productos. Para ello,
# basta con añadir otro campo a cada una de las sublistas:[columna, fila]

figuras = [["Cuadrados", 6, [3, 1]],
           ["Círculos", 5, [1, 2]],
           ["Triángulos", 4, [2, 2]],
           ["Rectángulos", 3, [4, 3]]]

# Imaginemos que se vende un cuadrado y hay que actualizar inventario:

figuras[0][1] = 5
for f in figuras:
    print(f"{f[0]}: Cantidad {f[1]} - Posición {f[2]}")
print()

# Imaginemos que queremos colocar todos los cuadrados en
# la columna 1, fila 3

figuras[0][2] = [1, 3]
for f in figuras:
    print(f"{f[0]}: Cantidad {f[1]} - Posición {f[2]}")
print()

# Imaginemos que queremos colocar todos los rectángulos en
# la columna 2, fila 3

figuras[3][2][0] = 2
for f in figuras:
    print(f"{f[0]}: Cantidad {f[1]} -->  Columna {f[2][0]}, Fila {f[2][1]}")
print()
