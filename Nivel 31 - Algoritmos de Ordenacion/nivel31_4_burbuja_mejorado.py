'''
Se intenta mejorar el algoritmo


lista = [5, 7, 3, 1, 8, 4, 9, 2, 6]

for i in range(len(lista)-1): # vueltas a dar
    for j in range(len(lista)-1): # ..para ir comparando los elementos..
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j] # invertimos por asignación múltiple
    print(lista)

[5, 3, 1, 7, 4, 8, 2, 6, 9]
[3, 1, 5, 4, 7, 2, 6, 8, 9]
[1, 3, 4, 5, 2, 6, 7, 8, 9]
[1, 3, 4, 2, 5, 6, 7, 8, 9]
[1, 3, 2, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]

en cada iteración, el mayor está al final y así sucesivamente, por lo que se pueden reducir
las iteraciones del bucle interno por cada una del bucle externo, y llega un momento que todo está ordenado,
sobrando iteraciones

'''

lista = [5, 7, 3, 1, 8, 4, 9, 2, 6]

hay_cambios = True
i = 0
while hay_cambios and i < len(lista)-1:
    hay_cambios = False
    for j in range(len(lista) -i -1): # reducimos verificar los ya ordenados
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j] 
            hay_cambios = True
    i += 1
print(lista)





