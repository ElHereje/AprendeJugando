'''
Antes de verlo, vemos  la suma recursiva:

lista = [2,3,4,5]

suma = 2 + [3,4,5]
            3 + [4,5]
                 4 + [5]
                      5 + []
                           0
        0
        5 + 0 = 5
        4 + 5 = 9
        3 + 9 = 12
        2 + 12 = 14
          
          
Para el caso de la resta:
          
lista = [2,3,4,5] --> resultado = 2 - 3 - 4 - 5 = -10

PRIMERA OPCIÓN:

resta = 2 - [3,4,5]
            3 - [4,5]
                 4 - [5]
                      5 - []
                           0
        0
        5 - 0 = 5
        4 - 5 = -1
        3 - (-1) = 4
        2 - 4 = -2   RESULTADO NO VÁLIDO
        
SEGUNDA OPCIÓN:

resta = [2,3,4] - 5
        [2,3] - 4
        [2] -3
        [] -2
        0
        
        0
        0 - 2 = -2
        -2 - 3 = -5
        -5 - 4 = -9
        -9 - 5 = -14   TAMPOCO ES VÁLIDO pq el caso base 
                        no es una lista vacía, por lo que:
                        
            "el caso base será que cuando lleguemos a la lista
            con un solo elemento, la resta de ese elemento menos ninguno
            más, será ese elemento", por lo que le esquema sería:

resta = [2,3,4] - 5
        [2,3] - 4
        [2] -3
         2
        
        2
        2 - 3 = -1
        -1 - 4 = -5
        -5 - 5 = -10  !!!

'''

lista = [2,3,4,5]
def resta(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return resta(lista[:-1]) - lista[-1]
    
print(resta(lista))