# TUPLE y LIST

# la función tuple forma un tupla con los objetos que le indicamos

a = tuple([1, 2, 3])
print(a)
print(type(a))

b = tuple(range(10))
print(b)

# La función list hace lo propio:

numeros = list(range(1, 11))
print(numeros)


# estas funciones también valen para crear listas o tuplas vacías

lista = list()  # --> []
tupla = tuple()  # --> ()
print(lista, tupla)

# En el caso de las listas, también nos vale para copiarlas

m = [1, 2, 3]
copia = m

print(m, copia)
m.append(4)
print(m, copia) # --> si modificamos una , también se modifica la copia.
                # --> [1, 2, 3, 4] [1, 2, 3, 4]

# para mantener una fija, lo que hacemos es:

q = list(m)
q.append(5)
print(m, q)  # --> [1, 2, 3, 4] [1, 2, 3, 4, 5]  solo se modifica la que queremos

