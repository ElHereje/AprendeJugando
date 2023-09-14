'''
Es un algoritmo intuitivo, también de complejodad cuadrática (n**2) y mas efectivo que
el de Selección.
Se comienzan a considerar los elementos desde el 2º, comparándolo con los que 
tienen delante.
'''

lista = [5, 7, 1, 3, 8, 4, 9, 2, 6]

for i in range(1, len(lista)):
    actual = lista[i]
    indice = i
    while indice > 0 and lista[indice - 1] > actual: 
        lista[indice] = lista[indice - 1] # vamos moviendo de posición hacia la izq.
        indice -= 1

    lista[indice] = actual

print(lista)