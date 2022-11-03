"""
Vamos a aplanar una lista, es decir, eliminar las listas internas.
Se forma una nueva lista simple con todos los elementos de la lista anidada
"""

datos = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
plana = []  # inicializamos una lista vacía

for lista in datos:
    for elemento in lista:
        plana.append(elemento)
print(plana)

# para otro tipo de datos que tienen elementos no iterables da error:
# problema para resolver en el siguiente video:
# datos2 = [[1, 2, 3], 4, 5, [6, 7], 8, 9]
# plana2 = []


# vamos a ver la función "type" y "isinstance"

a = 1
b = [1, 2, 3]
# para en el tipo de datos:
print(type(a))  # --> int
print(type(b))  # --> list

# isinstance toma 2 argumentos

print(isinstance(a, int))  # --> true
print(isinstance(b, list))  # --> true





