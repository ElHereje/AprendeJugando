"""
                    --CONJETURA DE COLLATZ-
Para todo nº entero positivo.
- Si es par se divide entre 2.
- si es par se multiplica por 3 y se suma 1.
Llavando a cabo estas operaciones sucesivamente sobre el nº
resultante, como resultado final siempre sale 1

--> 6  : 6-3-10-5-16-8-4-2-1
--> 11 : 11-34-17-52-36-13-40-20-10-5-16-8-4-2-1

1. Definir una función que compruebe que la conjetura se
cumple para cualquier nº
2. Comprobar  que se cumple para os nºs del 1 a un millón

"""

# apartado 1:
# def collatz(num):
#     secuencia = [num]
#     while num > 1:
#         if num % 2 == 0:
#             num //= 2
#         else:
#             num = num * 3 + 1
#         secuencia.append(num)
#     return secuencia
#
# secuencia = collatz(6)
# for i in secuencia:
#     print(i, end=' ')

# apartado 2:
def collatz(num):
    while num > 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
    if num == 1:
        return True
    else:
        return False

for i in range(1, 1_000_000):
    # para comprobar por donde va
    if i % 100_000 == 0:
        print(f"Comprobado hasta el {i}")
    if not collatz(i):
        print(f"no se cumple para el {i}")
        break
else:
    print("Se cumple para todos los nºs")