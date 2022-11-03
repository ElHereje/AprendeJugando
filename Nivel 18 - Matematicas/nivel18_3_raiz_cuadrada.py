"""
la función predefinida de python es sqrt(), del modulo math
"""
import math
x = math.sqrt(100)
print(x)


def raiz_cuadrada(num):
    # x * x = n
    x = 0
    while x*x <= num:
        x += 0.001  # cuanto más 0, más precisión, pero bastante más lento
    return x

print(raiz_cuadrada(100))

# para hacerlo más eficiente:
# (usaremos el método Babilónico)  --> SIGUIENTE VIDEO

