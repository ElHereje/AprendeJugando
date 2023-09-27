'''
En las lambda también podemos incluir condicionales:
'''

# para ordenar una tupla con carateres y números en base a los enteros:

datos = [(5, "a"), ("d", 3), ("e", 1), (2, "b"), ("c", 4)]

datos.sort(key= lambda x: x[0] if isinstance(x[0], int) else x[1])
print(datos)

# para hacerlo en base a las cadenas de caracteres:

datos.sort(key= lambda x: x[0] if isinstance(x[0], str) else x[1])
print(datos)


'''
RETO:

Tenemos una lista con números del 1 al 100.
Ordenar la lista primero con los múltiplos de 10,
y luego con los no múltiplos de 10.
Los nºs han de estar a su vez ordenados

datos = [40, 20, 51, 41, 30, 11, 50, 31, 10, 21]
'''