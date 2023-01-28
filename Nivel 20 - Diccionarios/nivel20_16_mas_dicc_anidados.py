"""
Desde el ejemplo anterior...
* Comprobar si algún miembro es de colombia y le gusta el rock
* Mostrar todos los miembros con sus aficiones
* Mostrar todos los datos de cada uno

"""
agenda = {
    "Jorge": {
        "Teléfono": 1111,
        "País": "Ecuador",
        "Personal": {
            "Afición": "Futbol",
            "Estudios": "Agronomía",
            "Música": "Clásica"
        }
    },
    "María": {
        "Teléfono": 2222,
        "País": "Colombia",
        "Personal": {
            "Afición": "Astronomía",
            "Estudios": "Informática",
            "Música": "Rock"
        }
    },
    "Tomás": {
        "Teléfono": 3333,
        "País": "Ecuador",
        "Personal": {
            "Afición": "Cine",
            "Estudios": "Informática",
            "Música": "Pop"
        }
    },
    "Carla": {
        "Teléfono": 4444,
        "País": "Colombia",
        "Personal": {
            "Afición": "Ajedrez",
            "Estudios": "Agronomía",
            "Música": "Clásica"
        }
    }
}

# * Comprobar si algún miembro es de colombia y le gusta el rock
for nombre, datos in agenda.items():
    if datos["País"] == "Colombia" and \
            datos["Personal"]["Música"] == "Rock":
        print(f"A {nombre} le gusta el rock...")

# * Mostrar todos los miembros con sus aficiones
for nombre, datos in agenda.items():
    print(f"{nombre}: {datos['Personal']['Afición']}")

# * Mostrar todos los datos personales de cada uno
for nombre, datos in agenda.items():
    print(f"Datos personales de {nombre}:")
    for categoria, informacion in datos['Personal'].items():
        print(f"  -{categoria}: {informacion}")
    print()
