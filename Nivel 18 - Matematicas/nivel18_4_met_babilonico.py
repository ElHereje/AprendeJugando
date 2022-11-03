"""
Es un método para calcular la raiz cuadrada
"""
# para comprobar...
import math

a = 81
print(math.sqrt(a))

def raiz_babilonica(n):
    x = n / 2  # suposición de partida

    for i in range(20):
        if x * x == n:
            return x
        else:
            x = (x + (n/x)) / 2
    return x

print(raiz_babilonica(81))

# esto podemos ajustarlo en el nivel de interacciones necesarias, debido a
# las limitaciones del tipo float

def raiz_babilonica_2(n):
    x = n / 2  # suposición de partida

    while True:
        if x * x == n:
            return x
        else:
            copia_x = x
            x = (x + (n/x)) / 2
        if copia_x == x:
            break
    return x

print(raiz_babilonica_2(81))