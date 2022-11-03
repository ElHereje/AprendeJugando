"""
Función que halle los múltiplos de un nº (algunos)
Función que halle los divisores de un nº (todos)
(Estamos en el ámbito de nºs enteros positivos)
"""

def multiplos_hasta_limite(numero, limite):
    '''halla los múltiplos hasta un límite dado'''
    multiplos = []
    i = 1
    multiplo = numero
    while multiplo <= limite:
        multiplos.append(multiplo)
        i += 1
        multiplo = numero * i
    return multiplos

def multiplos_hasta_cantidad(numero, cantidad):
    '''Halla la cantidad dada de múltiplos'''
    multiplos = []
    i = 1
    while len(multiplos) < cantidad:
        multiplo = numero * i
        multiplos.append(multiplo)
        i += 1
    return multiplos


# para el caso de los divisores:

def hallar_divisores(numero):
    '''halla los divisores de un número'''
    divisores = []
    for i in range(1, numero+1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

# num = int(input("Introduce nº: "))
# lim = int(input("Introduce límite: "))
# can = int(input("..o introduce una cantidad de múltiplos: "))
# print(multiplos_hasta_limite(num, lim))
# print(multiplos_hasta_cantidad(num, can))

print("Ahora los divisores...\n")
div = int(input("Introduce el número del cual quieres hallar los divisores: "))
print(hallar_divisores(div))