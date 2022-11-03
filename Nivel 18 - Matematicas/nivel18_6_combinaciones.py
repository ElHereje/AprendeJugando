'''
Calcula el numero de combinaciones sin repetición de n
elementos tomados de m en n.
Requiere de una función factorial

Conbinac. de m elementos tomados de n en n = m! / n! * (m-n)!
'''

# podemos usar la función predefinida en python o elaborada por nosotras.
import math

def combinaciones(m, n):
    if n > m:  # controlamos que m sea mayor
        return 0
    else:
        comb = math.factorial(m) / (math.factorial(n) * math.factorial(m - n))
    return comb

print(combinaciones(10, 5))


# hay una forma de reducir cálculos factoriales, que reduce los recursos consumidos:

def combinaciones2(m, n):
    diferencia = m - n
    f = 1
    while m > diferencia:
        f *= m
        m -= 1
    g = 1
    while n > 0:
        g *= n
        n -= 1
    return f / g

print(combinaciones2(10, 5))

