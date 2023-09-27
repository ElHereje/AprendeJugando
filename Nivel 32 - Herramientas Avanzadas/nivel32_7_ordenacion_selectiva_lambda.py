'''
RETO:

Tenemos una lista con números del 1 al 100.
Ordenar la lista primero con los múltiplos de 10,
y luego con los no múltiplos de 10.
Los nºs han de estar a su vez ordenados

datos = [40, 20, 51, 41, 30, 11, 50, 31, 10, 21]
'''

datos = [40, 20, 51, 41, 30, 11, 50, 31, 10, 21]

datos.sort(key= lambda x: x if x%10 == 0 else x+1000) # sumamos 100 para que esté fuera del rango

print(datos)

# Podríamos ordenar también diccionarios:


objetios_celestes = [
    {"Nombre": "Marte", "Tipo": "Planeta", "Diámetro": 6794},
    {"Nombre": "Europa", "Tipo": "Satélite", "Diámetro": 3121},
    {"Nombre": "Sol", "Tipo": "Etrella", "Diámetro": 1391016},
    {"Nombre": "Neptuno", "Tipo": "Planeta", "Diámetro": 49572},
    {"Nombre": "Ceres", "Tipo": "Asteroide", "Diámetro": 945},
    {"Nombre": "Luna", "Tipo": "Satélite", "Diámetro": 3476},
    {"Nombre": "Vesta", "Tipo": "Asteroide", "Diámetro": 530},
]

objetios_celestes.sort(key= lambda x: x["Diámetro"]) 

for objeto in objetios_celestes:
    print(objeto)



'''
RETO --> ordenra la lista por nombres en orden alfabético,
empezando por la m

nombres = ["Jorge", "Íñigo", "Alba", "María", "Cesar",
            "Marta", "Claudia", "Álvaro", "Paula", "Javier",
            "Silvia", "Ñuflo", "Azucena", "Irene", "Laura",
            "Zaira", "Añua", "Raúl", "Víctor", "Mario"] 
'''
