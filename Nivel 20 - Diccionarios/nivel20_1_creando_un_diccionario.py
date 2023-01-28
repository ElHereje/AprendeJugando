"""
DICCIONARIOS
"""

telefonos = {"José": 1234,
             "María": 3456,
             "Andrés": 5678,
             "Lucía": 9876}

# Operaciones básicas:

# consultar un valor:
print(telefonos["María"])

# comprobar si existe un valor:
print("Julia" in telefonos)  # dará true o false

# esto se haría con un condicional:
if "Julia" in telefonos:
    print(telefonos["Julia"])
else:
    print("Esa clave no existe.")

# agregar nuevos elementos
telefonos["Jorge"] = 6543
print(telefonos)

# modificar elementos del diccionario
telefonos["María"] = 7890
print(telefonos)

# eliminar elementos de un diccionario
del telefonos["Andrés"]
print(telefonos)
# !!Cuidado.. si no añadimos clave, borra todo el dicionario (del telefonos)

