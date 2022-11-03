"""
Haz un programa con una función que encuentre todos los nº primos
que hay en un intervalo de nºs indicados por el usuario
"""

def encuentra_primos(inicial, final):
    primos = []
    for n in range(inicial, final+1):
        contador = 0
        for i in range(1, n+1):
            if n % i == 0:
                contador += 1
        if contador == 2:
            primos.append(n)
    return primos


# podemos hacer esto mismo con las mismas modificaciones que el video anterior


def encuentra_primos2(inicial, final):
    primos =  []
    if inicial < 2:
        inicial = 2
    for n in range(inicial, final + 1):
        es_primo = True
        for i in range(2, n):
            if n % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(n)
    return primos


# también se puede hacer con una estructura especial de python FOR...ELSE

def encuentra_primos3(inicial, final):
    primos =  []
    if inicial < 2:
        inicial = 2
    for n in range(inicial, final + 1):
        for i in range(2, n):
            if n % i == 0:
                break
        else:  # SOLO SE EJECUTA SI EL FOR NO SALE CON EL BREAK
            primos.append(n)
    return primos


a = int(input("Introduce nº inicial: "))
b = int(input("Introduce nº final: "))
print(encuentra_primos(a, b))
print(encuentra_primos2(a, b))
print(encuentra_primos3(a, b))
