"""
ejemplo --> función sencilla que compruebe si un nº es impar
(va a devolver un valor lógico)
"""

def es_impar(num):
    if num % 2 != 0:
        resultado = True
    else:
        resultado = False
    return resultado

# una forma mas simple

def es_impar2(num):
    if num % 2 != 0:
        return True
    else:
        return False

# .. y aún mas reducida...

def es_impar3(num):
    if num % 2 != 0:
        return True  # --> la función sale al encontrar el primer return
    return False

n = int(input("Introduce un número: "))
if es_impar3(n):
    print("Es impar")
else:
    print("NO es impar")