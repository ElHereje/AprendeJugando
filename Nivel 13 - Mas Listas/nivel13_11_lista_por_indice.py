"""
crea o muestra por tipo de lista usando indices
"""

datos = [[1, 2, 3, 4],
         ["a", "b", "c", "d"],
         [5, 6, 7, 8],
         ["e", "f", "g", "h"],
         [9, 10, 11, 12],
         ["i", "j", "k", "l"],
         [13, 14, 15, 16],
         ["m", "m", "ñ", "o"],
         ]

numeros = []
letras = []

'''
de la manera del video anterior:
for objeto in datos:
    for lista in objeto:
        if isinstance(lista, int):
            numeros.append(lista)
        else:
            letras.append(lista)

print(numeros)
print(letras)'''

# vamos a imprimir los objetos en líneas independientes.
# luego, vamos a mostrar solo los elementos de las listas con letras.
# .. esas listas son las que tienen índice impar (1, 3, 5 y 7)
# para hacerlo por índices:
for i in range(len(datos)):  # iteramos por la lista
    for j in range(len(datos[i])):  # iteramos por cada sublista
        print(datos[i][j], end=" ")
    print()

print()
# 2ª parte:
for i in range(len(datos)):
    if i % 2 != 0:
        for j in range(len(datos[i])):
            print(datos[i][j], end=" ")
        print()
