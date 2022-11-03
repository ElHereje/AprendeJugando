# NONE significa un valor vacío

# ..pero no significa que sea igual a 0 o false.
# ..es simplemente igual a si mismo.
# se usa normalmente para dar valores iniciales a variables

# ***********************************************************

"""
numero = None

while numero != 5:
    numero = int(input("Dime un nº distinto de 5: "))
else:
    print("Has elegido el 5.")
"""

# ***********************************************************

# se suele usar normalmente con "is"

numero = None

while numero is None or numero > 5:
    numero = int(input("Dime un nº mayor que 5: "))
else:
    print("Has elegido un nº mayor que 5.")

# así hemos entrado en el bucle y respeta la 2ª condición
