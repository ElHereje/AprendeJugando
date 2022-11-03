"""
Encontrar los números repetidos de una lista
"""

lista = [2, 3, 5, 1, 4, 3, 6, 7, 9, 5, 8]
repetidos = []


# podemos hacerlo con 2 bucles for, pero no es muy eficiente (muy largo):
for i in range(len(lista)):
    for j in range(len(lista)):
        if i != j:  # para no comparar el mismo índice
            if lista[i] == lista[j] and lista[i] not in repetidos:
                repetidos.append(lista[i])
print(repetidos)

# otra manera más eficiente, ya que se recorre la lista una sola vez
repetidos2 = []
provisional = []
for numero in lista:
    if numero not in provisional:
        provisional.append(numero)
    else:
        repetidos2.append(numero)
print(repetidos2)
