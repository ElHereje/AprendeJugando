
# desempaquetar es asignar a cada uno de los valores de una
# lista o tupla, otro conjunto de valores.
# DEBE HABER LA MISMA CANTIDAD, y la asignación es por orden

(a, b) = (1, 2)
print(a)
print(b)
print()
c, d = 3, 4
print(c)
print(d)
print()
# esto también funciona en las listas

[x, y] = [10, 20]  # lista = lista
[j, k] = 30, 40  # lista = tupla
print(x)
print(y)
print()
print(j)
print(k)
print()

# si el nº de variables no es igual al de valores, dará error,
# a menos que se use el operador de desempaquetado --> "*"

u, d, *r = 1, 2, 3, 4
# así se asigna u=1, d=2, r = [3, 4]
print(u)
print(d)
print(r)
print()

# con una lista ...
numeros = [1, 2, 3, 4, 5]
uno, dos, *resto = numeros
print(uno)
print(dos)
print(resto)
print()

*one, two, rest = numeros
print(one)
print(two)
print(rest)
print()

# también podemos usar este operador para asignar varios valores
# a una sola variable

*s, = 1, 2, 3
print(s)
print()

# TODO ESTO VALE PARA OBTENER UN CÓDIGO MAS LEGIBLE
letras = ["A", "B", "C", "D", "E", "F", "G"]
primera = letras[0]
segunda = letras[1]
última = letras[-1]
resto = letras[2:-1]

print(primera)
print(segunda)
print(última)
print(resto)
print()

# esto puede reducirse....
primera, segunda, *resto, última = letras

print(primera)
print(segunda)
print(última)
print(resto)


