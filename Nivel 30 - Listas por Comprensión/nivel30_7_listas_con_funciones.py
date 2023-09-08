'''RETO --> Lista con los alumnos que hayan aprobado Lengua

alumnos = {"Claudia": {"Matemáticas":8, "Lengua":7, "Ingles":6},
           "Esteban": {"Matemáticas":7, "Lengua":3, "Ingles":8},
           "Silvia": {"Matemáticas":5, "Lengua":5, "Ingles":9},
           "Jorge": {"Matemáticas":3, "Lengua":4, "Ingles":5},
           "Roberto": {"Matemáticas":9, "Lengua":6, "Ingles":7}}



lista = [nombre for nombre, asignaturas in alumnos.items()
         if asignaturas["Lengua"]>=5]

lista2 = [nombre for nombre in alumnos if alumnos[nombre]["Lengua"]>=5]

print(lista)
print(lista2) '''

# Las listas cpor comprensión también nos valen para modificar
# otras listas de manera rápida y directa

valores_decimales = [1.2342432423, 2.34523432, 3.45283765756]

# para redondear los decimales:
redondeados = [round(v, 2) for v in valores_decimales]
print(redondeados)

# pasar a mayúsculas
minus = ["mesa", "silla", "puerta", "ventana", "armario"]
mayus = [palabra.upper() for palabra in minus]
print(mayus)

# cálculos
import math
radios = [7, 12, 21, 32, 41]
area = [math.pi*r**r for r in radios]
print(area)