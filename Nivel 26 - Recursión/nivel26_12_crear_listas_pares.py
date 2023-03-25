'''
Crear una lista de forma recursiva con los números pares de 
entre 2 números dados
'''


def lista_pares(inicio, final):
    # caso base --> inicio >= final
    if inicio > final:
        return []
    elif inicio % 2 == 0:
        return [inicio] + lista_pares(inicio+1, final)
    else:
        return lista_pares(inicio+1, final)
    
    
print(lista_pares(2, 10))
