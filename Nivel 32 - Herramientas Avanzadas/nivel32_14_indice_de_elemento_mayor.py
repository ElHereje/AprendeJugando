'''Dada una lista:

1. Hallar el índice de la primera coincidencia del número mayor
2. Hallar los índices de todas las coincidencias del número mayor'''

numeros = [43, 27, 58, 12, 39, 58, 54, 33, 21, 58, 17, 46]

# 1 --> en este caso el índice será 2

i_mayor = max(enumerate(numeros), key= lambda x:x[1]) # el lambda pq queremos el mayor nº no el mayor indice
print(i_mayor) # --> (2, 58)

# otra manera es con el método index():
i_mayor_2 = numeros.index(max(numeros))
print(i_mayor_2) # --> 2

# 2

i_mayores = [i for i, n in enumerate(numeros) if n == max(numeros)]
print(i_mayores) # --> [2, 5, 9]