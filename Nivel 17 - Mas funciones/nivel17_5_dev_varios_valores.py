
def operaciones(n):
    doble = n*2
    triple = n*3
    return doble, triple

resultado = operaciones(5)
print(resultado)  # devuelve una tupla --> (10, 15)

# también podemos recuperar los valores independientes:
d, t = operaciones(5)
print(d)
print(t)

