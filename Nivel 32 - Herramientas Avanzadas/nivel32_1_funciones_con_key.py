'''
Vamos a ver las herramienbtas usadas para los procedimientos vistos en el curso

'''

datos =  [257, 573, -714, 321, -158, 642, 407]

# para el valor máximo atendiendo al valor absoluto
print(max(datos, key=abs)) # -714
# para el minimo igual...
print(min(datos, key=abs)) # -158

# para ordenamieto de secuencias...
print(sorted(datos)) # [-714, -158, 257, 321, 407, 573, 642]
# para hacerlo a la inversa..
print(sorted(datos, reverse=True)) # [642, 573, 407, 321, 257, -158, -714]
# ... y en función del valor absoluto
print(sorted(datos, key=abs)) # [-158, 257, 321, 407, 573, 642, -714]



# en el caso de las listas:
cadenas = ["kkkkk", "hhhhhh", "jjj", "qqqqqqqqq", "tttt"]

print(max(cadenas)) # tttt
print(min(cadenas)) # hhhhhh
# por nº de caracteres:
print(max(cadenas, key=len)) # qqqqqqqqq
print(min(cadenas, key=len)) # jjj

# si lo que queremos es ordenar por longitud:
print(sorted(cadenas, key=len)) # ['jjj', 'tttt', 'kkkkk', 'hhhhhh', 'qqqqqqqqq']


# para el caso de tuplas de 2 elementos
datos = [(7, 20), (6, 30), (4, 50), (8, 10), (5, 40)]

print(max(datos)) # se valora el indice 0 de cada elemento --> (8, 10)

# si queremos el mayor pero con el indice 1, no existe funcion predef.
# pero la podemos crear...

def indice_uno(secuencia):
    return secuencia[1]

print(max(datos, key=indice_uno)) # (4, 50)
print(min(datos, key=indice_uno)) # (8, 10)
# si queremos ordenar por ese indice:
print(sorted(datos, key=indice_uno)) # [(8, 10), (7, 20), (6, 30), (5, 40), (4, 50)]


'''
RETO:
datos = [(4, 2, 1), (5, 4, 2), (2, 1, 3), (3, 0, 1), (3, 4, 2)]

1 - Ordenar de menor a mayor según la suma de sus elementos
2 - Ordenar de menor a mayor teniendo en cuenta el elemento 3, desp el 2 y luego el 1

'''