"""
Programa que simula una calculadora, usando funciones.
Que tenga las opciones de sumar, restar, multiplicar y dividir.
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
    print("5. Salir.")
    opc = input("--> ")
    return opc


def pedir_datos():
    termino1 = float(input("Introduce Primer término: "))
    termino2 = float(input("Introduce Segundo término: "))
    return termino1, termino2  # varios valores --> nivel17_5


def mostrar_resultado(opc, resultado):
    print()
    print(f"El resultado de la {opc} es {resultado}")


while True:
    opc = menu()
    if opc == "5":
        break
    elif opc == "1" or opc == "2" or opc == "3" or opc == "4":
        t1, t2 = pedir_datos()  # varios valores --> nivel17_5
        if opc == "1":
            operacion = "Suma"
            resultado = suma(t1, t2)
        if opc == "2":
            operacion = "Resta"
            resultado = resta(t1, t2)
        if opc == "3":
            operacion = "Multiplicación"
            resultado = multi(t1, t2)
        if opc == "4":
            operacion = "División"
            resultado = divi(t1, t2)
        mostrar_resultado(operacion, resultado)
    else:
        print("Opción incorrecta...")