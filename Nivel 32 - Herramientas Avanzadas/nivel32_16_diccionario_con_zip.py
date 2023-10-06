'''
----------- RETO PARA RESOLVER -----------

Crear un diccionario cuyas claves sean los nombres de los alumnos,
y cuyos valores sean las notas medias de las tres notas parciales.
'''

nombres = ["Jorge", "Sara", "Lucía", "Andrés", "Miguel"]
primero = [5,7,3,5,4]
segundo = [7,9,5,6,3]
tercero = [6,8,4,7,2]

# manera 1
notas = {}
for n, p, s, t in zip(nombres, primero, segundo, tercero):
    notas[n] = (p + s + t) / 3

for nombre, nota in notas.items():
    print(f"{nombre:8}: {nota:2.1f}")


# manera 2 (agrupamos las 3 listas y luego agrupamos notas y medias)
medias = [ (p+s+t)/3 for (p,s,t) in zip(primero, segundo, tercero)]
notas2 = dict(zip(notas, medias))
for nombre, nota in notas2.items():
    print(f"{nombre:8}: {nota:2.1f}")