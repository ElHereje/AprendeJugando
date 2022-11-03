# MANIPULANDO CADENAS

# REALIZAN CIERTO TIPO DE FUNCIONES, ESTANDO SIEMPRE ASOCIADOS
# A UN TIPO DE OBJETO

cadena = "artefacto nuevo"

print(cadena.upper())  # --> devuelve una nueva cadena de caracteres, este caso, en mayúsculas

otra_cadena = "ARTILUGIO"

print(otra_cadena.lower())  # --> artilugio
print(cadena.title())  # --> Artefacto Nuevo
print(cadena.capitalize())  # -->  Artefacto nuevo

# util para pasar a minúscula respuestas de usuario

respuesta = input("¿Quieres seguir jugando (s/n)?: ")
if respuesta.lower() == "s":
    print("Vale...")


'''
Programa de ejemplo que utiliza los 3 métodos
'''

nombre = input("Hola, ¿Quien eres?: ")
print(f"Hola {nombre.title()}")
confirma = input(f"¿Seguro que eres {nombre.upper()}?: ")
if confirma.lower() == "s":
    print("Vale")
else:
    print("No te entiendo...")
