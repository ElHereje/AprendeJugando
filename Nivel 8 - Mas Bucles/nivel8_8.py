'''
Programa que comprueba si un elemento está en una lista
y nos dice su posición (índice).
Usar tipo RANGE para recorrer la lista por sus índices.
'''

lista = [2, 5, 90, 23, 45, 87, 54, 11, 38]
elemento = 54

for i in range(len(lista)):
    if lista[i] == elemento:
        print(f"Está en la posición {i}")


"""
programa que muestre la tabla de multiplicar de un número
que le demos
"""

numero = int(input("Dime un número: "))
for i in range(11):
    print(f"{numero} X {i} = {numero * i}")