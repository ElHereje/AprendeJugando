"""
Crea una nueva lista que sea el reverso de la dada
"""

numeros = [1, 5, 8, 4, 7, 2, 9]

reverso = list()

# Forma 1
'''for i in range(len(numeros)):
    reverso.append(numeros[len(numeros) - 1 - i])
    print(reverso)'''
# Forma 2
'''for n in numeros:
    reverso = [n] + reverso  # añadimos el nuevo elemento + lo que había
    print(reverso)  # --> para comprobar como se va formando'''

# Forma 3
'''reverso = numeros[::-1]  # desde el último:hasta el primero:con salto -1'''

# Forma 4
numeros.reverse()  # --> [9, 2, 7, 4, 8, 5, 1]
            # PERO NO ES UNA NUEVA, SINO EL REVERSO DE LA MISMA
print(numeros)

'''
Crea una lista "cuenta_adelante" que contenga los elementos
de la lista "cuenta_atras" pero en orden inverso.
Utiliza el método reverse()
'''

cuenta_atras = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# primero copiamos la original, para no modificar la original
cuenta_adelante = list(cuenta_atras)
cuenta_adelante.reverse()
print(cuenta_adelante)
