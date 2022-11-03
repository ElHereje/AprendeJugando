"""
Vamos a comprobar si un nº es primo (nºs enteros solo divisibles
por si mismo o por 1) :

2 es divisible por 2 y por 1 -->  ES PRIMO
3 es divisible por 3 y por 1 --> ES PRIMO
4 es divisible por 4, por 2 y por 1 --> NO ES PRIMO
5 es divisible por 5 y por 1 --> ES PRIMO
6 es divisible por 6, por 3, por 2 y por 1 --> NO ES PRIMO

No se van a tomar en cuneta los números negativos.

"""
def es_primo(num):
    contador = 0
    for i in range(1, num + 1):
        if num % i == 0:
            contador += 1
    if contador == 2:  # por sí mismo y por 1
        return True
    else:
        return False


"""
Otra opción es que el rango vaya desde 2 hasta num, y no (1, n+1).
de esta manera no se encuentra ni el 1 ni el mismo nº, por lo que no
debe haber ningún nº primo en ese rango
"""


def es_primo2(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True # else


numero = int(input("Introduce un número: "))
print(es_primo(numero))
print(es_primo2(numero))

#  se va a optimizar esta función en el próximo video

