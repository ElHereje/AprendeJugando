'''
Vamos a ver el ordenamiento con el Particionado de Hoare: una version en la que los 
intercamnbios se llevan a cabo en la misma lista, sin listas auxiliares, y que sigue 
la estrategia de particionado original de QuickSort
'''

def particionado(lista, menor, mayor):

    pivote = lista[menor] # primer elemento de la lista
    izq = menor + 1 # a continuación del pivote
    der = mayor 

    while True:
        while izq <= der and lista[izq] <= pivote:
            izq += 1 # movemos el puntero una posición
        while izq <= der and lista[der] >= pivote:
            der -= 1
        if der < izq:
            break # salimos del bucle
        else:
            lista[izq], lista[der] = lista[der], lista[izq]
    
    lista[menor], lista[der] = lista[der], lista[menor]
    
    return der  # que será el punto que divide las listas de menores y mayores que el pivote


def quicksort(lista, menor, mayor):
    if menor < mayor: # es decir...si tiene mas de un elemento...
        pivote = particionado(lista, menor, mayor)
        quicksort(lista, menor, pivote-1) # parte izq
        quicksort(lista, pivote+1, mayor) # pqarte derecha

lista = [9, 1, 4, 9, 3, -1, 15, 12, 3, 9, -3, 7, 5, 2, 10]

print(lista)
quicksort(lista, 0, len(lista)-1)
print(lista)