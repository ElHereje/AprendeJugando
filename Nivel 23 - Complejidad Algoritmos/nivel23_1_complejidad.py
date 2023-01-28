'''

NOTACIÓN ASINTÓTICA

Complejidad de tiempo "O GRANDE"

Un ejemplo es la anécdota de GAUSS:

sunmar los 100 1os números

en vez de 100 operaciones, se dió cuanta que sumando el 1º
y el último dá 101, el 2º y penúltimo tb 101...
por lo que 50*101=5050

en resumen --> suma de Nºs --> (n/2) * (n+1) con solo 1 operación


como ejercicio para el siguiente video:
Definir 2 funciones para calcular la suma del 1 a n números.
Una de ellas sumando uno a uno, y otra aplicando la fórmula de gauss:


import time

def suma_lineal(n):
    pass

def suma_constante(n):
    pass
    
cantidad = 1000000

for i in range(4):
    
    t0 = time.time()
    suma1 = suma_lineal(cantidad)
    t1 = time.time()
    suma2 = suma_constante(cantidad)
    t2 = time.time()
    
    print(f"{suma1} - {t1-t0}")
    print(f"{suma2} - {t2-t1}")
    
    cantidad *= 10 # multiplicamos la cantidad por 10 en la siguiente iteración



'''