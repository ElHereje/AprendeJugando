"""
Define una función que tome 3 números y devuelva el que sea
el intermedio. Si hay repetidos, se devuelve el repetido.
Si hay 3 repetidos, el único que hay.

Pruebas:

print(numero_intermedio(1, 2, 3))
print(numero_intermedio(3, 2, 1))
print(numero_intermedio(2, 3, 1))
print(numero_intermedio(3, 1, 2))
print(numero_intermedio(1, 3, 2))
print(numero_intermedio(2, 1, 3))
print(numero_intermedio(2, 2, 3))
print(numero_intermedio(2, 3, 2))
print(numero_intermedio(3, 2, 2))
print(numero_intermedio(2, 2, 1))
print(numero_intermedio(2, 1, 2))
print(numero_intermedio(1, 2, 2))
print(numero_intermedio(2, 2, 2))



"""


def numero_intermedio(a, b, c):
    '''función que toma 3 números y
    devuelve el valor intermedio'''

    if a <= b <= c or c <= b <= a:
        return b
    elif b <= a <= c or c <= a <= b:
        return a
    elif a <= c <= b or b <= c <= a:
        return c


print(numero_intermedio(1, 2, 3))
print(numero_intermedio(3, 2, 1))
print(numero_intermedio(2, 3, 1))
print(numero_intermedio(3, 1, 2))
print(numero_intermedio(1, 3, 2))
print(numero_intermedio(2, 1, 3))
print(numero_intermedio(2, 2, 3))
print(numero_intermedio(2, 3, 2))
print(numero_intermedio(3, 2, 2))
print(numero_intermedio(2, 2, 1))
print(numero_intermedio(2, 1, 2))
print(numero_intermedio(1, 2, 2))
print(numero_intermedio(2, 2, 2))