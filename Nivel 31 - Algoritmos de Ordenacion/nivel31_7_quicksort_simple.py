
lista =  [8, 12, 3, 11, 5, 9, 10, 4, 10, 15, 7]

# vamos a necesitar una función auxiliar que divida la lista:
def particionado(lista):
    pivote = lista[0] # vamos a coger el 1er elemento
    menores = []
    mayores = []
    for i in range(1, len(lista)):
        if lista[i] < pivote:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])

    return menores, pivote, mayores


def quicksort(lista):
    if len(lista) < 2 : # caso base
        return lista
    
    menores, pivote, mayores = particionado(lista)
    return quicksort(menores) + [pivote] + quicksort(mayores)

print(quicksort(lista))
