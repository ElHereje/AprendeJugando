'''
Función que halle de fora recursiva el resultado
de sumar los nºs pares de una lista
- Estrategia 1: por sublistas
- Estrategia 2: por índices
'''

lista = [3, 4, 5, 8, 9, 12]

def sumar_pares_por_sublista(lista):
    if lista == []: # len(lista) == 0
        return 0
    elif lista[0] % 2 == 0:
        return lista[0] + sumar_pares_por_sublista(lista[1:])
    else:
        return sumar_pares_por_sublista(lista[1:])
    

def sumar_por_indices(lista, i=0, suma=0):
    if len(lista) == i:
        return suma
    elif lista[i] % 2 == 0:
        suma += lista[i]
    
    return sumar_por_indices(lista, i+1, suma)
    
    
print(sumar_pares_por_sublista(lista))
print(sumar_por_indices(lista))
