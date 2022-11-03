"""
            -- Conjetura de Goldbach --
Todo nº par mayor que 2 se puede expresar como
la suma de dos nºs primos.

Para el nº 14 tendríamos: 3 y 11, 7 y 7
(1 y 13 no vale, ya que el 1 no es considerado como primo)

Hacer un programa que muestre todas las parejas de primos
en las que se puede expresar un nº par mayor que 2

"""
# podemos usar la función ya usada (def es_primo(n))

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Numero par mayor que 2: "))

# solo es para los pares:
if num % 2 == 0 and num > 2:
    for a in range(2, num):
        if es_primo(a):
            b = num - a
            if es_primo(b):
                if a <= b:  # (para que no se repitan las parejas)
                    print(f"Primos {a} {b}")
else:
    print(f"{num} no es un nº válido")