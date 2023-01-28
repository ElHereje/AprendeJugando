

agenda = {
    "Jorge": {
        "Teléfono": 1111,
        "País": "Ecuador",
        "Aficiones": ["Futbol", "Leer"]
    },
    "María": {
        "Teléfono": 2222,
        "País": "Colombia",
        "Aficiones": ["Astronomía", "Natación"]
    },
    "Tomás": {
        "Teléfono": 3333,
        "País": "España",
        "Aficiones": ["Cine", "Pasear"]
    },
    "Carla": {
        "Teléfono": 4444,
        "País": "México",
        "Aficiones": ["Ajedrez", "Karate"]
    }
}

# para saber el país de María:
pais_maria = agenda["María"]["País"]
print(pais_maria)

aficiones_carla = agenda["Carla"]["Aficiones"]
for aficion in aficiones_carla:
    print(aficion)

# para recorrer el diccionario para extraer distintos datos
for nombre, datos in agenda.items():
    print(f"{nombre}: {datos['País']}")

    