"""
Defina un función que concatene 2 cadenas de caracteres,
las veces que le indiquemos.

Hacer un programa que pida dos cadenas de caracteres y las veces que
han de repetirse, y mostrar el resultado.
"""

def concatena(cad1, cad2, veces):
    return veces * (cad1 + cad2)

c1 = input("Introduce cadena 1: ")
c2 = input("Introduce cadena 2: ")
v = int(input("Introduce el nº de veces: "))

cadena = concatena(c1, c2, v)
print(cadena)