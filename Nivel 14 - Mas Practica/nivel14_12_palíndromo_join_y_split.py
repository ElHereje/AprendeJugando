

# vamos a hacerlo primero por el método JOIN

# Pasamos a minúsculas y separamos las palabras
minus = cadena.lower()
palabras = minus.split()  # -> crea una lista con todas las palabras
print(palabras)  # para ir viendo como va...

# quitamos las comas y puntos
lista_plana = []
for p in palabras:
    q = p.strip(".").strip(",")
    lista_plana.append(q)
print(lista_plana)  # para ir viendo como va...

# creamos una sola cadena con los elementos de la lista
cadena_plana = "".join(lista_plana)
print(cadena_plana)  # para ir viendo como va...

# quitamos las tildes
cadena_final = cadena_plana.replace("á", "a").replace("é", "e")\
    .replace("í", "i").replace("ó", "o").replace("ú", "u")
print(cadena_final)  # para ir viendo como va...

reverso = cadena_final[::-1]
print(reverso)

# comparamos las dos cadenas
if cadena_final == reverso:
    print("Son PALÍNDROMOS")
else:
    print("NO son PALÍNDROMOS")
