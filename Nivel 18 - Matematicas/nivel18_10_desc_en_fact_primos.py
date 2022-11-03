"""
Función que descompone un nº en los factores primos
de los que está compuesto

(puede valer, por ejemplo, para hallar em MCD)
"""

def descomponer(numero):
    primos = []
    for i in range(2, numero+1):
        while numero % i == 0:  # si es divisible...
            primos.append(i)
            numero = numero / i
    return primos


num = int(input("Introduce nº a descomponer: "))
print(descomponer(num))
