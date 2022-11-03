"""
Haz un programa en el que se compruebe si un número
es múltiplo de otro, mediante una función con 2 return
"""


def es_multiplo(multiplo, num):
    if multiplo % num == 0 :
        return True
    return False


multiplo = int(input("Numero a comprobar : "))
num = int(input("Si es múltiplo de : "))


if es_multiplo(multiplo, num):
    print(f"{num} es múltiplo de {multiplo}")
else:
    print(f"{num} NO es múltiplo de {multiplo}")
