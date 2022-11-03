"""
En el caso de la potencia:
"""

y = 3
print(y**3)
print(pow(y, 3))

"""
Definir una función que haga lo mismos que la función pow()
"""

def potencia(base, exponente):
    resultado = 1
    for i in range(exponente):
        resultado *= base
    return resultado

print(potencia(3, 3))