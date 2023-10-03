'''
ITERABLES (se pueden recorrer)
---------
listas --> list = [1,2,3,4,5]
tuplas 
cadenas
range
diccionarios
sets


ITERADORES (permiten recorrer los elementos de una colecc. de datos)
----------
iter() + next()
reversed()
enumerate()
zip()
filter()
map()

'''

a = iter(range(10)) # al acceder a sus elementos, se van eliminando
print(next(a)) # --> 1
print(next(a)) # --> 2
print("----")
for i in a:
    print(i)