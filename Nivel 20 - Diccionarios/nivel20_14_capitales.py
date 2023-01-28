"""
Programa para repasar las capitales

Requisitos
    - Los paises han de salir de manera aleatoria.
    - Si se falla se muestra la capital.
    - Al final vuelven a salir los fallados.
    - Se sigue hasta que se acierten todos.
"""

import random

capitales = {
    "Canadá": "Ottawa",
    "Uruguay": "Montevideo",
    "kenia": "Nairobi",
    "Islandia": "Reikiavik",
    "Filipinas": "Manila"
    }

# creamos una lista para que los paises salgan de manera aleatoria
paises = list(capitales.keys())

print("--- REPASAR CAPIALES ---")
print("------------------------")

while len(paises) > 0: # mientras que tenga algún elemento...
    fallos = []
    random.shuffle(paises)
    for pais in paises:
        print()
        print(f"La capital de {pais} es: ")
        intento = input("--> ")
        if intento == capitales[pais]:
            print("Has acertado!")
        else:
            print(f"Era {capitales[pais]}!")
            fallos.append(pais)
        print()
        input("Enter para continuar")
    paises = fallos
else:
    print("HAs terminado el repaso")
