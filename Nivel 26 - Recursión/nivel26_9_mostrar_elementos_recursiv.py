# función que muestre los elementos de la lista de manera recursiva

lista = [1, 3, 5, 7, 9, 11]

def mostrar_1(lista):

    # caso base --> lista = []
    if len(lista) != 0:
        print(lista[0])
        mostrar_1(lista[1:])

def mostrar_2(lista, indice=0):

    if indice != len(lista):
        print(lista[indice])
        mostrar_2(lista, indice+1)

mostrar_1(lista)
mostrar_2(lista)


