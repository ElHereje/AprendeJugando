"""
Hacer un programa que calcule la nota (en base a 10 puntos) de un
examen que puede tener distinta cantidad de preguntas, y por cada
fallo se reste una cierta cantidad de puntos.
"""

def nota(preguntas, aciertos, penalizacion):
    nota = (aciertos * (10/preguntas)) - (preguntas - aciertos) * penalizacion
    return nota

preguntas = int(input("¿ Cuantas preguntas hay ? :  "))
aciertos = int(input("¿Cuantos aciertos? : "))
penalizacion = float(input("¿Que penalización tiene cada fallo?: "))

nota_final = nota(preguntas, aciertos, penalizacion)
print(f"La nota final del alumno es {nota_final}")