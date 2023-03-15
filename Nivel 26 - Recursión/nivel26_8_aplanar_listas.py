'''
Aplanar una listas anidada de cualquier dimensión.

datos = [[1,2],[[3,4],[[[5,6],[[7,8],[9,10]]],[11,12]]]]

'''

datos = [[1,2],[[3,4],[[[5,6],[[7,8],[9,10]]],[11,12]]]]


def aplanar_iterativa(lista):
    plana = []
    # hacemos una copia de la lista original
    pila = list(lista)
    while len(pila) > 0: # mientras haya elementos...
        dato = pila.pop() # sacamos un elemento y lo guardamos en dato
        if type(dato) == int:
            plana.append(dato)
        else:
            for elemento in dato:
                if type(elemento) == int:
                    plana.append(elemento)
                else:
                    # volvemos a guardarla en la pila
                    pila.append(elemento)
    return (sorted(plana))


def aplanar_recursiva(lista):
    plana2 = []
    for elemento in lista:
        if type(elemento) == int:
            plana2.append(elemento)
        else:
            plana2 = plana2 + aplanar_recursiva(elemento)
    return plana2 # los devuelve ya ordenados...


# esto lo podemos optimizar

def aplanar(lista):
    plana2 = []
    for elemento in lista:
        if type(elemento) in (int, str, float, tuple):
            plana2.append(elemento)
        else:
            plana2.extend(aplanar(elemento))
    return plana2 # los devuelve ya ordenados...



print(aplanar_iterativa(datos))
print(aplanar_recursiva(datos))
print(aplanar(datos))
        

