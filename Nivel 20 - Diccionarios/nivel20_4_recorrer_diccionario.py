


telefonos = {
    "José": 1234,
     "María": 3456,
     "Andrés": 5678,
     "Lucía": 9876
    }

# Para mostrar las claves del diccionario:
# for clave in telefonos:
#     print(clave)

# for clave in telefonos:
#     print(clave, ": ", telefonos[clave])

# Existen métodos para esto (keys, values, items):

# Para obtener las claves:
vista_clave = telefonos.keys()
print(vista_clave)  #--> dict_keys(['José', 'María', 'Andrés', 'Lucía'])
# para convertir lo anterior en una lista cn las claves del diccionario
vista_clave2 = list(telefonos.keys())
print(vista_clave2)  # --> ['José', 'María', 'Andrés', 'Lucía']

# para obtener una vista de los valores --> values
print(telefonos.values())  # --> dict_values([1234, 3456, 5678, 9876])
# también lo podemos ver como lista
print(list(telefonos.values()))  # --> [1234, 3456, 5678, 9876]
# con este método podemos ver si un valor está en el diccionario
if 1234 in telefonos.values():
    print("Ese valor está en el diccionario.")
# podemos iterar por los valores:
for valor in telefonos.values():
    print(valor)

# con el método "items" vemos las parejas clave:valor en tuplas:
print(telefonos.items())
for elemento in telefonos.items():
    print(elemento) # --> así se ve en forma de tuplas
# para verlos en una forma más formateada:
for elemento in telefonos.items():
    print(elemento[0], elemento[1])
# esto se puede hacer de una manera más elegante:
for clave, valor in telefonos.items():
    print(clave,":", valor)