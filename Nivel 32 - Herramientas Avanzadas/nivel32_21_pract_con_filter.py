'''
Reto para resolver:

1. Crear una lista con metales con valor >= que 10.
2. Crear una lista con metales con valor >= que 10
   y que tengan "e" en su nombre.

'''

metales = {
    "Hierro": "2",
    "Plata": "23",
    "Zinc": "7",
    "Cobre": "11",
    "Aluminio": "4",
    "Plomo": "15",
    "Oro": "30"
    }

# 1 con filter
seleccion = list(filter(lambda x: int(metales[x]) >= 10, metales))
print(seleccion)
# 1 con comprension
seleccion2 = [x for x in metales if int(metales[x])>= 10]
print(seleccion2)

# 2 con filter
seleccion3 = list(filter(lambda x: "e" in x, seleccion))
print(seleccion3)
#.... hemos usado el filter anterior, pero si no lo ponemos, quedaría:
seleccion4 = list(filter(
    lambda x: "e" in x, filter(
        lambda x: int(metales[x]) >= 10, metales)))
print(seleccion4)
# .... igual pero reducido
seleccion5 = list(filter(lambda x: int(metales[x]) >= 10 and "e" in x, metales))
print(seleccion5)

# 2 por lkistas por comprension
seleccion6 = [x for x in metales if int(metales[x])>= 10 and "e" in x]
print(seleccion6)


