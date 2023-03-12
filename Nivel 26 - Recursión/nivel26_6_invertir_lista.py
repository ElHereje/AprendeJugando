'''
Invertir una lista de manera recursiva:

lista = [1,2,3,4,5] --> inversa = [5,4,3,2,1]

'''

lista = [1,2,3,4,5]

def inversa(lista):
    if lista == []:
        return lista
    else:
        return inversa(lista[1:]) + lista[:1]
    
print(inversa(lista))
