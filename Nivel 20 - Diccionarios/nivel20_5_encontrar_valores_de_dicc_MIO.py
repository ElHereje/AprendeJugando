"""
Repetir el ejemplo de la agenda de videos anteriores, pero con las opciones
y usando métodos

1. Consultar por nombre
2. Consultar por teléfono
3. Listar la agenda
4. Salir

"""

telefonos = {"José": 1234,
             "María": 3456,
             "Andrés": 5678,
             "Lucía": 9876}

vista_nom = list(telefonos.keys())
vista_tel = list(telefonos.values())


def consulta_por_nombre(nom):
    i=0
    encontrado = ""
    for nombre in vista_nom:
        if nombre == nom:
            print(nombre, ":", vista_tel[i])
            encontrado = True
        i += 1
    if not encontrado:
        print("No existe esa entrada")
        

def consulta_por_telefono(tel):
    i = 0
    encontrado = ""
    for telefono in telefonos.values():
        if tel == telefono:
            print(vista_nom[i], ":", telefono)
            encontrado = True
        i += 1
    if not encontrado:
        print("No existe esa entrada")


def listar():
    for clave, valor in telefonos.items():
        print(clave, ":", valor)


consultando = True

while consultando:
    print()
    print("MIS TELÉFONOS")
    print("-------------")
    print("1. Consultar por nombre")
    print("2. Consultar por teléfono")
    print("3. Listar la agenda")
    print("4. Salir")
    print("-------------")

    opcion = ""
    while opcion not in ("1", "2", "3", "4", "5"):
        opcion = input("-> ")

    if opcion == "1":
        nom = input("Introduce nombre: ")
        consulta_por_nombre(nom)

    elif opcion == "2":
        tel = int(input("Introduce teléfono: "))
        consulta_por_telefono(tel)

    elif opcion == "3":
        listar()

    elif opcion == "4":
        consultando = False

