'''
RETO:
ordenar de forma alfabética independientemente de may, acentos,...
'''

palabras = ["isla", "último", "Ángela", "Italia",
            "índice", "Íñigo", "óptica", "árbol",
            "Úrsula", "época", "Olmedo", "Uruguay",
            "Elvira", "ukelele", "Argentina", "Écija",
            "Óscar", "amapola", "elefante", "objeto"]

# si usamos solo sort, lo hace por UNICODE
# con sort(key= str.lower) no incluye las tildes.
# con una lambda:

palabras.sort(key= lambda p: p.lower().replace("á","a").\
              replace("é","e").replace("í","i").\
                replace("ó","o").replace("ú","u").\
                    replace("ñ", "nzz").replace("ü", "u"))

print(palabras)

'''
RETO:
Dada una lista con los datos de una maratón, que contiene: nº de dorsal, nombre y tiempo empleado,
se necesita orden según el tiempo empleado.

'''
resultados = [
    ["101", "Alicia", "03:20:05"],
    ["102", "Alberto", "03:20:01"],
    ["103", "Jorge", "03:20:04"],
    ["104", "Susana", "03:20:07"],
    ["105", "Roberto", "03:20:06"],
    ["106", "Silvia", "03:20:04"],
    ["107", "Ignacio", "03:20:02"],
    ["108", "Raquel", "03:20:03"]
    ]

resultados.sort(key= lambda x: (int(x[2][:2])*360 + \
                                int(x[2][3:5])*60 + \
                                int(x[2][6:])))

for r in resultados:
    print(r)