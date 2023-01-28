'''
Una empresa de autopistas tiene instalada una cámara que cuenta el nº
de vehículos que pasa por un aautopista, y tiene instaladas unas gomas que 
cuenta el nº de ruedas d elos vehículos que pasan.

La empresa quiere contratar un programador que elabore un algoritmo
que a partir del nº de vehículos y el nº de ruedas, extraiga la cantidad de 
coches y motos que pasan.

elaborar el algoritmo con la menor comlejidad

vehículos = coches + motos
ruedas = coches*4 + motos*2

'''

#Algoritmo O(n**2)
def extraccion_1(vehiculos, ruedas):
    
    for coches in range(vehiculos + 1):
        for motos in range(vehiculos + 1):
            if ((coches + motos) == vehiculos) and ((coches*4 + motos*2) == ruedas):
                return coches, motos
    return None
    # este es un procedimiento por fuerza bruta muy poco eficiente, ya
    # que contiene 2 bucles for
    
#Algoritmo O(n)
def extraccion_2(vehiculos, ruedas):
    
    for coches in range(vehiculos + 1):
        motos = vehiculos - coches
        if coches * 4 + motos * 2 == ruedas:
            return coches, motos
    return None
    # solo usamos un bucle for, por lo que es mas eficiente
    
'''Aún podemos simplificar mas sustituyendo variables

        motos = vehiculos - coches
    ruedas = coches*4 + (vehiculos-coches)*2
    coches*2 + vehículos - coches = ruedas/2
    
        coches = ruedas/2 - vehículos

'''
#Algoritmo constante O(1)
def extraccion_3(vehiculos, ruedas):
    
    coches = ruedas/2 - vehiculos
    motos = vehiculos - coches
    
    if int(coches) + int(motos) == vehiculos:
        return int(coches), int(motos)
    else:
        return None

