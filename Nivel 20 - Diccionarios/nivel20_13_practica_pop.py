'''
Programa que gestiona el pago de deudas

deudas = {
    "Jorge": "4C",
    "Isabel": "3B",
    "Ana": "1D",
    "Miguel": "5E",
    "Sara": "2A"
}

while True:
    print("1. Saldar deuda")
    print("2. Ver entradas")
    print("3. Ver total de deuda")
    print("4. Salir")
'''

deudas = {
    "Jorge": 12,
    "Isabel": 20,
    "Ana": 10,
    "Miguel": 8,
    "Sara": 15
}

total = sum(list(deudas.values()))  # suma de todos los valores

while True:
    print("1. Saldar deuda")
    print("2. Ver entradas")
    print("3. Ver total de deuda")
    print("4. Salir")

    posibles = (1, 2, 3, 4)
    entrada = ""
    while entrada not in posibles:
        entrada = int(input("opción -> "))
    if entrada == 1:
        nombre = input("Nombre a saldar: ")
        saldado = deudas.pop(nombre, 0)  # si no existe, toma como valor 0
        total -= saldado
        if saldado == 0:
            print("No hay deudas para ese nombre")
        else:
            print(f"Se han saldado {saldado}€")
            print()
    elif entrada == 2:
        print()
        for nombre, debo in deudas.items():
            print(f"{nombre}: {debo}")
        print()
    elif entrada == 3:
        print(f"El total de la deuda es de {total}€")
        print()
    elif entrada == 4:
        break


