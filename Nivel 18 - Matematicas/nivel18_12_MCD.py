"""
Función que calcule el MCD de 2 números

mcd --> mayor de los divisores comunes de esos números:

div 20 = 1, 2, 4, 5, 10, 20
div 12 = 1, 2, 3, 4, 6, 12

div comunes = 1, 2, 4 --> mcd = 4

"""

# por divisores comunes.
# aprovechamos la función del video anterior:
def hallar_divisores(numero):
    divisores = []
    for i in range(1, numero+1):
        if numero % i == 0:
            divisores.append(i)
    return divisores


def mcd_divisores_comunes(n1, n2):
    # hallamos los divisores de los 2 números
    d1 = hallar_divisores(n1)
    d2 = hallar_divisores(n2)

    # vamos verificando datos:
    print(f"Divisores de 1: {d1}")
    print(f"Divisores de 2: {d2}")
    # extraemos los comunes a los 2
    comunes = []
    for i in d1:
        if i in d2:
            comunes.append(i)

    # vamos verificando datos:
    print(comunes)

    # elegimos el mayor
    mcd = comunes[-1]  # cogemos el último elemento
    return mcd


a = int(input("Introduce nº 1: "))
b = int(input("Introduce nº 2: "))
print(f"El MCD de {a} y {b} es {mcd_divisores_comunes(a, b)}")


# esta función no es muy efeciente, ya que hay que llevar a cabo muchas operaciones:

# podemos hacerlo por fuerza bruta, es decir, recorrer todos
# los nº posibles hasta encontrar en mcd
# el mcd será un nº menor o igual que el menor de los que se comparan

