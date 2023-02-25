'''
las matrices son conjuntos de datos, generalmente numéricos, ordenados en
filas y columnas.

Python no dispone del tipo matriz, pero podemos simularlas con listas 
bidimensionales.

por ejemplo, para representar el consumo en una granja:

            trigo   cebada  pienso  paja
    Vacas   21      18      35      40
    Cerdos  19      11      21      14
    Ovejas  12      15      20      30

'''
# lista anidada que hace las veces de matriz
consumo = [[21, 18, 35, 40],
           [19, 11, 21, 14],
           [12, 15, 20, 30]]

# para ver los datos:
for lista in consumo:
    print("[", end=" ")
    for elemento in lista:
        print(elemento, end=" ")
    print("]")
# El resultado sería:
# [ 21 18 35 40 ]
# [ 19 11 21 14 ]
# [ 12 15 20 30 ]


# si necesitamos una matriz cero, podemos diseñarla manualmente:
mc = [[0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0]]

# si queremos una matriz cero con las dimensiones fullHD... se tardaría mucho tiempo
# por lo que nos interesa crearla con un algoritmo --> video siguiente
           
    