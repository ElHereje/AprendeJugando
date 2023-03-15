'''
Invertir una lista de manera recursiva:

lista = [1,2,3,4,5] --> inversa = [5,4,3,2,1]

En resumen, lo que se hace es eliminar el último elemento y posicionarlo en primer lugar

lista = [1,2] --> [2] + [1]
lista = [1] --> [1] + []
lista = [] --> []  -> caso base

lista = [1,2,3] --> [3]+[1,2] --> [3]+[2]+[1]



lista = [1,2,3,4,5]

def inversa(lst):
    # Caso base
    if lst == []:
        return lst
    # Caso recursivo
    else:
        return inversa(lst[1:]) + lst[:1]
    
print(inversa(lista))

def inversa_2(lst):
    # Caso base
    if len(lst) == 0:
        return []
    # Caso recursivo
    else:
        return [lst[-1]] + inversa_2(lst[:-1])

print(inversa_2(lista))

'''

lista = [1,2,3,4,5]

# def invertir_lista(lista):
#     if lista == []:
#         inversa = lista
#     else:
#         inversa = [lista[-1]] + invertir_lista(lista[:-1]) # último + el resto (al que hacemos recursiva)
#     return inversa

# esto podemos optimizarlo:
def invertir_lista(lista):
    if lista == []:
        return lista
    else:
        return [lista[-1]] + invertir_lista(lista[:-1])
    
print(invertir_lista(lista))
