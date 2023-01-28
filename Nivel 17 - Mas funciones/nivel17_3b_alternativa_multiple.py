"""
Es el mismo programa pero con la opción de continuar
operando con el último resultado:
"""

def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multi(a, b):
    return a * b


def divi(a, b):
    return a / b


def menu():
    print()
    print(f"Cálculo Múltiple. El primer término es {n1}")
    print("---------------------------")
    print("Introduce Opción (1-4): ")
    print("1. Sumar.")
    print("2. Restar.")
    print("3. Multiplicar.")
    print("4. Dividir.")
    opc = input("--> ")
    return opc

n1 = float(input("Introduce nº 1: "))

while True:
    opc = menu()
    n2 = float(input("Introduce nº 2: "))
    if opc == "1":
        resultado = suma(n1, n2)
    elif opc == "2":
        resultado = resta(n1, n2)
    elif opc == "3":
        resultado = multi(n1, n2)
    elif opc == "4":
        resultado = divi(n1, n2)

    print(f"El resultado es {resultado}")

    n1 = resultado  # para seguir operando.

    seguir = input("¿Continuar operando? (s/n) : ")

    if seguir == "n":
        break