'''
Sumar los elementos de una lista con una función de manera recursiva

lista = [1, 2, 3, 4, 5]

hacerlo de una manera iterativa es sencillo:

def sumar(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma


Para hacerlo de manera recursiva, lo 1º es buscar el caso base.
Lo mas simple es el caso de una lista vacía

lista = [] --> suma = 0
lista = [10] --> suma = 10 + suma[0]
lista = [10, 20] --> suma = 10 + suma[20] --> 10 + 20 + suma[]
lista = [10, 20, 30] --> suma = 10 + suma[20 + 30] --> 10 + 20 + suma[30]
...

en nuestro caso
suma = 1 + [2,3,4,5]
            2 + [3+4+5]
                3 + [4+5]
                    4 + [5]
                        5 + []


En nuestro caso:
                        
lista = [1, 2, 3, 4, 5]

def sumar(lista):
    if lista == []:
        suma = 0
    else:
        suma = lista[0] + sumar(lista[1:])
    return suma
print(sumar(lista))

'''
# esta función optimizada quedaría como:

lista = [1, 2, 3, 4, 5]

def sumar(lista):
    if lista == []:
        return 0
    else:
        return lista[0] + sumar(lista[1:]) # sacamos el 1º y sumamos el resto...
    
print(sumar(lista))
