'''
EJERCICIO

Crear una lista co el tipo de dato de cada uno
de los elementos de la lista datos:
- si son cadenas de caracteres: "cadena"
- si son enteros o float: "numérico"

datos = [7, "h", 2.5, "m", 8.2, 24, "p"]
'''

'''datos = [7, "h", 2.5, "m", 8.2, 24, "p"]
tipos = ["cadena" if type(dato)==str else
         "numerico" for dato in datos]
print(tipos)'''

# tambien podemos crearlas a partir de listas anidadas

personas = [["Jorge", 36], ["Silvia",24], ["Tomás", 47],
            ["Irene", 19], ["Ignacio", 21], ["Julia", 43],
            ["Sara", 38], ["Miguel", 25]]

# nueva con las personas mayores de 30
mayores = [persona for persona in personas if persona[1] > 30]
print(mayores)

# si solo queremos los nombres:
nombres = [persona[0] for persona in personas if persona[1] > 30]
print(nombres)

'''
Reto --> lista con toda la información de "personas", pero con "mayor" 
si es mayor de 30 o "menor" si no lo es
'''