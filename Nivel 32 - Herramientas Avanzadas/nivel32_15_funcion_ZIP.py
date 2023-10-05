'''
Básicamente, esta función lo que hace es combinar los elementos de los diferentes
iterables que se le pase, devolviendo un objeto iterador que nos va devilviendo
tuplas con los elementos correspond a cada uno de los iterables polr el ñíndice que 
ocupa.
Si alguna tiene más elementos que la otra, se para al agotares los pares

'''

alumnos = ["Jorge", "Sara", "Lucía", "Andrés", "Miguel"]
edades = [25, 19, 31, 28, 42]

datos_alumnos = zip(alumnos, edades)
for dato in datos_alumnos:
    print(dato)
    """ ('Jorge', 25)
        ('Sara', 19)
        ('Lucía', 31)
        ('Andrés', 28)
        ('Miguel', 42)
    """

# si tenemos una lista más con las notas y queremos agruparlas

notas = [7.4, 8.3, 9.2, 6.5, 5.8]

# ceamos un nuevo iterable, o reutilizamos el anterior.
datos_alumnos_2 = zip(alumnos, edades, notas)

for a, e, n in datos_alumnos_2:
    print(f"El alumno {a}, de {e} años, ha obtenido un {n}")

# para una lista con estas tuplas:
print(list(zip(alumnos, edades, notas)))

# ESTA FUNCIÓN ACEPTA VARIOS TIPOS DE ITERABLES:
minusc = "abcde"
mayusc = ["A", "B", "C", "D", "E"]
numero = range(1, 6)

grupo = zip(mayusc, minusc, numero)

for g in grupo:
    print(g)

'''
----------- RETO PARA RESOLVER -----------

Crear un diccionario cuyas claves sean los nombres de los alumnos,
y cuyos valores sean las notas medias de las tres notas parciales.


nombres = ["Jorge", "Sara", "Lucía", "Andrés", "Miguel"]
primero = [5,7,3,5,4]
segundo = [7,9,5,6,3]
tercero = [6,8,4,7,2]

'''