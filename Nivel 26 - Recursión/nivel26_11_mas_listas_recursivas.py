'''
Crear de forma recursiva una lista con orden ascendente
que contenga los cuadrados de los números que estén incluidos
en el intervalo de 2 números dados: 3 y 7: [9, 16, 25, 36, 49]
'''

def lista_cuadrados(inicio, final):
    # caso base --> inicio >= final
    if inicio > final:
        return []
    else:
        return [inicio**2] + lista_cuadrados(inicio+1, final)
    


# para hacerlo con métosos:
def lista_cuadrados_metodos(inicio, final, a=[]):
    # caso base --> inicio >= final
    if inicio > final:
        return a
    else:
        a.append(inicio**2)
        return lista_cuadrados_metodos(inicio+1, final, a)
    
print(lista_cuadrados(3, 7))
print(lista_cuadrados_metodos(3, 7))




