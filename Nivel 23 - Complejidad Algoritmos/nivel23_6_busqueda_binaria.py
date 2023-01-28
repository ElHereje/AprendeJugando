'''
vamos a ver un nuevo algoritmo de búsqueda, el binario

se necesita una lista ordenada de datos
complejidad O(log n)

1º debemos comprobar si el elemento que está en la mitad es el que buscamos, 
si no lo es ,comprobamos si es mayor o menor descartando el trozo contrario
y volvemos a repetir la operación... así hasta dar con el buscado.

inicio=0        medio = (inicio + final) // 2       final = len(lista) - 1

----------------------------------------------------------------------------
                                    |
           final = medio - 1        |          inicio = medio + 1

'''

# vamos a ver esto en código

datos = [2, 3, 5, 6, 8, 11, 12, 15, 17, 18, 21, 23, 24, 29, 30]
buscado = 23

def busqueda_binaria(lista, elemento):
    ''' True si está, False si no'''
    
    pasos = 0
    inicio = 0
    final = len(lista) - 1
    
    while inicio <= final:
        
        #para ver cuantos pasos necesitamos
        pasos += 1
        
        medio = (inicio + final) // 2
        if lista[medio] == elemento:
            return True, pasos
        elif lista[medio] < elemento:
            inicio = medio + 1
        elif lista[medio] > elemento:
            final = medio - 1
            
    return False, pasos


print(busqueda_binaria(datos, buscado))