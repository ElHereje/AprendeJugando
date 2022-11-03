# vamos a ver una de las consecuencias que ocurren con las listas
# anidadas , al ser un tipo mutable

m = [1, 2, 3]
n = m  # seguimos teniendo el mismo objeto, no una nueva copia

# esto no podríamos hacerlo si queremos guardar el valor original.
# para hacerlo, sería:

n = m[:]  # --> crea un nuevo objeto.

# también a traves de la función list

s = list(m)  # crea una nueva lista con los elementos de m

# con las listas anidadas:

p = [1, [2, 3], [4, 5]]

#  para hacer una copia de p:

q = list(p)

print(p)
print(q)
print()
p[0] = 10
p[1][0] = 20
p[2][0] = 40

print(p)
print(q)

# el resultado será:
# [1, [2, 3], [4, 5]]
# [1, [2, 3], [4, 5]]
#
# [10, [20, 3], [40, 5]]
# [1, [20, 3], [40, 5]]

# vemos que las listas interiores también se han modificado
# al hacer esto, python lo que hace es una referencia al mismo objeto.

# veremos como hacerlo en el siguiente video

