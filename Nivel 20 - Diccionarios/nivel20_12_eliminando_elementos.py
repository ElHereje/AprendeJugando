
alumnos = {
    "Jorge": "4C",
    "Isabel": "3B",
    "Ana": "1D",
    "Miguel": "5E",
    "Sara": "2A"
}
print(alumnos)
# DEL
# para eliminar desde la clave --> DEL
del alumnos["Miguel"]
print(alumnos)
# SI SE USA DEL CON UNA CLAVE QUE NO EXISTE, DÁ ERROR

# POP
# devuelve el valor asociado a la clave eliminada
nombre = alumnos.pop("Isabel")
print()
print(alumnos)
print(nombre) # --> 3B
# si no existe, podemos poner un 2º parámetro
nombre2 = alumnos.pop("José", "No existe")
print(alumnos)
print(nombre2) # --> no existe

# POPITEM()
# SI EL DICCIONARIO ESTÁ VACÍO, DARÁ ERROR
# NO FUNCIONA SI ESTAMOS ITERANDO DENTRO DEL DICCIONARIO
# (podríamos si fuera un range --> for clave in range(len(alumnos)) )
# Elimina el último valor
# No devuelve un valor, sino una tupla clave:valor
nombre3 = alumnos.popitem()
print()
print(alumnos)
print(nombre3)
# podemos asociar cada dato a una variable
nom, clase = alumnos.popitem()
print()
print(alumnos)
print(nom, clase)
