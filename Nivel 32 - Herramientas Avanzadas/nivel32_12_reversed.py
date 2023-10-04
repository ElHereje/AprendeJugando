'''



'''
lista= [1,2,3,4,5]
reverso = list(reversed(lista)) # se crea una nueva lista con el contenido indicado
print(reverso)


# podemos recorrer las listas con uyn while, pero con cuidado de las escepciones.

rever = reversed(lista)

while True:
    try:
        elemento = next(rever)
        if elemento == 1:
            print(elemento)
    except StopIteration:
        break

# 

reve = reversed(lista)
lista.clear() # --> hemos vaciado el iterador
next(reve) # ERROR StopIteration
