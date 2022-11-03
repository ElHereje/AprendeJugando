"""
Encuentra el número mayor y el número menor de una lista.
(La lista puede contener enteros positivos y negativos).

Se debería probar con varias listas que contengan solo positivos,
positivos y negativos y solo negativos.

Sería conveniente no usar las funciones predefinidas max y min.
"""

# numeros = [29, 37, 41, 7, 25, 18, 11, 12, 42, 21]
# numeros = [-23, 27, -16, 11, 32, -35, 48, 6, -1, 17]
numeros = [-15, -7, -22, -37, -2, -28, -5, -19, -12, -21]

mayor = None
menor = None
for n in numeros:
    if mayor is None or n > mayor:
        mayor = n
    if menor is None or n < menor:
        menor = n
print(mayor)
print(menor)

