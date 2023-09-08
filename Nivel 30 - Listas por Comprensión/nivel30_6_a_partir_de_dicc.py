'''
Reto --> lista con toda la información de "personas", pero con "mayor" 
si es mayor de 30 o "menor" si no lo es

personas = [["Jorge", 36], ["Silvia",24], ["Tomás", 47],
            ["Irene", 19], ["Ignacio", 21], ["Julia", 43],
            ["Sara", 38], ["Miguel", 25]]
'''

personas = [["Jorge", 36], ["Silvia",24], ["Tomás", 47],
            ["Irene", 19], ["Ignacio", 21], ["Julia", 43],
            ["Sara", 38], ["Miguel", 25]]

lista = [[p[0], "Mayor"] if p[1]>30 else
         [p[0], "Menor"] for p in personas]
print(lista)

lista2 = [[p[0], "Mayor" if p[1]>30 else "Menor"] for p in personas]
print(lista2)

# SE PUEDEN REALIZAR LISTA TAMBIÉN A PARTIR DE DICCIONARIOS

inventario = {"Clavos": 30,
              "Tornillos": 140,
              "Tuercas": 250,
              "Arandelas": 70}

pedido = [articulo for articulo in inventario if inventario[articulo] < 100]
print(pedido)
pedido2 = [clave for clave, valor in inventario.items() if valor < 100]
print(pedido2)


# LISTAS CON DICCIONARIOS

alumnos = [{"Nombre":"Claudia", "Nota":9, "Grupo":"A"},
           {"Nombre":"Esteban", "Nota":4, "Grupo":"B"},
           {"Nombre":"Silvia", "Nota":7, "Grupo":"C"},
           {"Nombre":"Jorge", "Nota":3, "Grupo":"B"},
           {"Nombre":"Roberto", "Nota":6, "Grupo":"A"},]
# crear lista con los alumnos aprobados
aprobados = [a["Nombre"] for a in alumnos if a["Nota"] >= 5]
print(aprobados)

'''RETO --> Lista con los alumnos que hayan aprobado Lengua

alumnos = {"Claudia": {"Matemáticas":8, "Lengua":7, "Ingles":6},
           "Esteban": {"Matemáticas":7, "Lengua":3, "Ingles":8},
           "Silvia": {"Matemáticas":5, "Lengua":5, "Ingles":9},
           "Jorge": {"Matemáticas":3, "Lengua":4, "Ingles":5},
           "Roberto": {"Matemáticas":9, "Lengua":6, "Ingles":7}}'''