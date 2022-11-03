"""
Definir función en la que a un nº (minuendo) se le reste
 otro (sustraendo) las veces que se indique (veces)

--> 100 - (5 * 3) al 100 se le resta 5 3 veces = 85

"""


def operac(minuendo, sustraendo, veces):
    return minuendo - (sustraendo * veces)

numero = float(input("Dime un número: "))
restar = float(input("Por cual lo quieres restar: "))
repeticiones = int(input("Cuantas Veces: "))

resultado = operac(numero, restar, repeticiones)

print(resultado)
