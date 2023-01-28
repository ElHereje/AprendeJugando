telefonos = {"José": 1234,
             "María": 3456,
             "Andrés": 5678,
             "Lucía": 9876}

vista_nom = list(telefonos.keys())
vista_tel = list(telefonos.values())

print(vista_nom)

nom = input("Nombre: ")
i=0

encontrado = True
while encontrado:
    if nom in vista_nom:
        print("SIII")
        print(nom, ":" ,vista_tel[i])
        break
    else:
        print("NOO")
        encontrado = False
    i += 1



