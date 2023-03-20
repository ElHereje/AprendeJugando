'''
Crear de forma recursiva una lista de números enteros descendiente
desde un número dado hasta cero
'''

def crear_descendiente(n):

    # caso base --> n=0
    if n == 0:
        return [0]
    else:
        return [n] + crear_descendiente(n-1)
    
def crear_ascendente(n):
    
    # caso base --> n=0
    if n == 0:
        return [0]
    else:
        return crear_ascendente(n-1) + [n]
    
def crear_con_metodos(n, a=[]):

    if n < 0:
        return a
    else:
        a.append(n)
        return crear_con_metodos(n-1, a)

    
print(crear_descendiente(20))
print(crear_ascendente(20))
print(crear_con_metodos(20))

