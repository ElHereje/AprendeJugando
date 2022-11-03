"""
Lo que vamos a realizar es unir los programas anteriores.
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
    print("Introduce Opción (1-5): ")
    print("1. Sumar.")
    print("2. Restar.")
    print("3. Multiplicar.")
    print("4. Dividir.")
    opc = input("--> ")
    return opc


def calcular (opc, n1, n2):
    if opc == "1":
        resultado = suma(n1, n2)
    elif opc == "2":
        resultado = resta(n1, n2)
    elif opc == "3":
        resultado = multi(n1, n2)
    elif opc == "4":
        resultado = divi(n1, n2)
    return resultado


def tipo_calculo():
    print("1. Cálculo Único.")
    print("2. Cálculo Múltiple.")
    tipo = input("-->  ")
    return tipo

def calculo_unico():
    print("CÁLCULO ÚNICO")
    while True:
        opc = menu()
        n1 = float(input("Introduce nº 1: "))
        n2 = float(input("Introduce nº 2: "))
        resultado = calcular(opc, n1, n2)
        print(f"Resultado : {resultado}")
        seguir = input("¿Seguir operando...?? (s/n) : ")
        if seguir == "n":
            break

def calculo_multiple():
    print("CÁLCULO MÚLTIPLE")
    n1 = float(input("Introduce nº 1: "))
    while True:
        opc = menu()
        n2 = float(input("Introduce nº 2: "))
        resultado = calcular(opc, n1, n2)
        print(f"Resultado : {resultado}")
        n1 = resultado
        seguir = input("¿Seguir operando...? (s/n) : ")
        if seguir == "n":
            break


def main():
    eleccion = tipo_calculo()
    if eleccion == "1":
        calculo_unico()
    elif eleccion == "2":
        calculo_multiple()


# PROGRAMA PRINCIPAL:

main()

