"""
En un examen hay 40 preguntas, y cada fallo quita 0,10 puntos.
Hacer una función que calcule la nota (con base en 10 puntos) a partir de
las preguntas acertadas.
"""

def nota_final(aciertos):
    # nota = acierto - fallos
    # regla de 3--> si 40 son 10 ptos....1 es 0,25
    nota = (aciertos * 0.25) - (40 - aciertos) * 0.10
    return nota

aciertos = int(input("Introduce aciertos: "))

nota = nota_final(aciertos)
print(f"La nota final del usuario es {nota}")



