"""
Se trata de repetir el programa que determinaba el nº intermedio, pero
incluyendo otras funciones:

def numero_intermedio(a, b, c):
    '''función que toma 3 números y
    devuelve el valor intermedio'''

    if a <= b <= c or c <= b <= a:
        return b
    elif b <= a <= c or c <= a <= b:
        return a
    elif a <= c <= b or b <= c <= a:
        return c

"""

def mayor(a, b):
    if a > b:
        return a
    else:
        return b


def menor(a, b):
    if a < b:
        return a
    else:
        return b

# def numero_intermedio(a, b, c):
#     '''función que toma 3 números y
#     devuelve el valor intermedio'''
#     if a < b:
#         m =menor(b, c)
#         n = mayor(m, a)
#         return n
#     else:
#         m = menor(a, c)
#         n = mayor(m, b)
#         return n


# esto podría resumirse en :

def numero_intermedio(a, b, c):
    '''función que toma 3 números y
    devuelve el valor intermedio'''
    if a < b:
        return mayor(a, menor(b, c))
    else:
        return mayor(b, menor(a, c))


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