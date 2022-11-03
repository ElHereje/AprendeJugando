"""
Programa que convierte temperaturas:
ºFahrenheit a ºCelsius y viceversa.
ºF = (ºC * 1.8) + 32  //  ºC = (ºF - 32)/1.8

debe contener la siguiente estructura de funciones

def cels_a_fahr():
    pass

def fahr_a_cels():
    pass

def menu():
    pass

def pedir_grados():
    pass

def mostrar_resultado():
    pass

while True:

Añadir la posibilidad de salida de bucle
y la de que no teclee una opción correcta

 """


def cels_a_fahr(cel):
    return (cel * 1.8) + 32


def fahr_a_cels(fah):
    return (fah - 32)/1.8


def menu():
    print()
    print("Introduce Opción (1-3): ")
    print("1. Pasar a Celsius.")
    print("2. Pasar a Fahrenheit.")
    print("3. Salir.")
    opc = input("--> ")
    return opc


def pedir_grados(selec):
    '''
    Función que pide datos por pantalla
    :param selec: opción elegida
    :return: devuelve un input, en este caso los grados a convertir
    '''
    if selec == "1":
        grados = float(input("Introduce ºF: "))
    elif selec == "2":
        grados = float(input("Introduce ºC: "))
    return grados


def mostrar_resultado(selec, grados):
    '''
    Función que coge la opción seleccionada (selec) y devuelve
    una cadena formateada con el resultado (grados)
    '''
    if selec == "1":
        print(f"Son {grados} Celsius.")
    elif selec == "2":
        print(f"Son {grados} Fahrenheit.")


while True:
    opc = menu()
    if opc == "3":
        break
    elif opc == "1" or opc == "2":
        gr = pedir_grados(opc)
        if opc == "1":
            conversion = fahr_a_cels(gr)
        if opc == "2":
            conversion = cels_a_fahr(gr)
        mostrar_resultado(opc, conversion)
    else:
        print("Opción incorrecta...")

