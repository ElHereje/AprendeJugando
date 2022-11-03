# vamos a aplanar una lista que distinto tipo de datos

datos2 = [[1, 2, 3], 4, 5, [6, 7], 8, 9]
plana2 = []

for objeto in datos2:
    # if isinstance(datos2, list) --> otra manera 
    if type(objeto) == list:
        for elemento in objeto:
            plana2.append(elemento)
    else:
        plana2.append(objeto)
print(plana2)

