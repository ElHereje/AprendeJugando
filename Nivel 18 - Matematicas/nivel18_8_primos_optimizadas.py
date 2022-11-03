"""
def es_primo2(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
"""
import time, math

def es_primo2(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True



"""
Por propiedades matemáticas, la raiz cuadrada de un nº marca
el punto de inflexión a partir del cual los factores se 
empiezan a repetir

1 * 64 = 64
2 * 32 = 64
4 * 16 = 64
8 * 8 = 64  --> Los factores comienzan a repetirse
16 * 4 = 64
32 * 2 = 64
64 * 1 = 64

esto significa que solo habrá que llegar hasta este punto

todo nº compuesto por dos factores:
uno de ellos será menor o igual a la raiz cuadrada de ese nº,
y el otro será mayor o igual a la raiz de ese nº.

PRUEBA: por reducción al absurdo (o contradicción)

    Un nº n es igual al producto de los factores a*b
    Si a>raiz cuadrada de n y b>raiz cuadrada de n:
        (si los dos son mayores, o menors, la prueba será igual)
    Entonces: a*b > raiz cuadrada de n * raiz cuadrada de n
        Lo cual quiere decir que a * b > n
    Con lo que llegamos a un absurdo, que contradice la suposición
    de la que partimos 
    
    
con esto llegamos que solo hay que llegar hasta el valor redondeado
de la raiz de ese nº, acortándose en tiempo.


"""

def es_primo3(num):
    if num < 2:
        return False
    raiz = int(math.sqrt(num))+1
    for i in range(2, raiz):
        if num % i == 0:
            return False
    return True


t0_a = time.time()
resultado = es_primo2(123457897)
t1_a = time.time()
t0_b = time.time()
resultado2 = es_primo3(123457897)
t1_b = time.time()
print(f"Resultado sin optimizar --> {resultado}, {t1_a - t0_a}")
print(f"Resultado optimizado --> {resultado2}, {t1_b - t0_b}")
