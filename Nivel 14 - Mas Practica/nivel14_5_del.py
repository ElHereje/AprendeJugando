"""
Esta sentencia no solo elimina elementos de una lista, sino
también variables.
Lo que hace realmente es desvincular el objeto de la variable, y python
(en concreto el recolector de basura), elimina el objeto para liberar
la memoria que ocupaba.
"del" es una sentencia, NO una función predefinida, aunque puede
usarse con paréntesis (... son redundantes ...)
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8]

del lista[0]
print(lista)  # --> [2, 3, 4, 5]

# con "del" podemos eliminar elementos de una lista a través de su índice
# e incluso segmentos de dicha lista:

del lista[2:5] # elimina desde el índice 2 hasta el 5 (no incluido)
print(lista)

# también se puede usar para vaciar una
# lista (aunque es mejor usar "clear")

