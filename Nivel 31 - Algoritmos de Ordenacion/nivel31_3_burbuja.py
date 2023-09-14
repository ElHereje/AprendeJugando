'''
Recorremos cada elemento y lo comparamos con el que tiende delante. si es menor, se intercambia.
Se itera desde el primer emento hasta la long. de la lista - 1
'''

lista = [5, 7, 1, 3, 8, 4, 9, 2, 6]

for i in range(len(lista)-1): # vueltas a dar
    for j in range(len(lista)-1): # ..para ir comparando los elementos..
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j] # invertimos poer asignación múltiple
print(lista)

'''
Son muchas operaciones las que realiza, lo que lo convierte en un algoritmo muy poco eficiente.
'''