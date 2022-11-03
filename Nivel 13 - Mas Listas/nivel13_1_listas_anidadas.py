nombres = ["Susana", "Rubén", "Clara", "Jorge"]
edades = [18, 19, 20, 21]

# podemos organizar esta información a través de listas anidadas:

'''amigos = [["Susana", 18], ["Rubén", 19], ["Clara", 20], ["Jorge", 21]]'''

# para visualizar mejor este tipo de  listas, se ponen cada lista en una linea:

amigos = [["Susana", 18],
          ["Rubén", 19],
          ["Clara", 20],
          ["Jorge", 21]]
print(amigos)

# para acceder y modificar a cada lista:
print(amigos[0])

# para accede , por ejemplo a la edad de Rubén:
print(amigos[1][1]) # --> índice 1 del índice 1

# para actualizar (modificar un dato...
amigos[3][1] = 22
print(amigos[3])

# para añadir un item...
amigos.append(["Sara"])
print(amigos)
amigos[4].append(22)
print(amigos)


# podemos mostrar los datos de manera mas organizada con un for.
for amigo in amigos:
    print(f"{amigo[0]} : {amigo[1]} años.")
