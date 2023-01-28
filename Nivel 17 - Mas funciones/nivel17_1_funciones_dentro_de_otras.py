#  ejemplo -->  print(len(max("abc", "aeiu", "sdjkh")))  # --> 5

# esto mismo lo podemos realizar a la hora de diseñar nuestras funciones:

# función que determina el mayor de 3 numeros

# def mayor_de_tres(a, b, c):
#     '''Función que toma 3 números y devuelve el mayor'''
#     mayor = a
#     if b > mayor:
#         mayor = b
#     if c > mayor:
#         mayor = c
#     return mayor


# esta misma función podemos hacerla llamando a otras funciones dentro

def mayor_de_dos(a, b):
    if a > b:
        return a
    else:
        return b

# def mayor_de_tres(a, b, c):
#     m = mayor_de_dos(a, b)
#     if m > c:
#         return m
#     else:
#         return c


# Otra menra de hacerlo....
# def mayor_de_tres(a, b, c):
#     m = mayor_de_dos(a, b)
#     n = mayor_de_dos(m, c)
#     return n


# ...incluso tendríamos otra manera....
def mayor_de_tres(a, b, c):
    return mayor_de_dos(a, mayor_de_dos(b, c))

# Pruebas:

print(mayor_de_tres(1, 2, 3))
print(mayor_de_tres(3, 2, 1))
print(mayor_de_tres(2, 3, 1))
print(mayor_de_tres(3, 1, 2))
print(mayor_de_tres(1, 3, 2))
print(mayor_de_tres(2, 1, 3))
print(mayor_de_tres(2, 2, 3))
print(mayor_de_tres(2, 3, 2))
print(mayor_de_tres(3, 2, 2))
print(mayor_de_tres(2, 2, 1))
print(mayor_de_tres(2, 1, 2))
print(mayor_de_tres(1, 2, 2))
print(mayor_de_tres(2, 2, 2))

