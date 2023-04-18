
from superheroe import Superheroe
from arma import Arma

martillo = Arma("Martillo", 6, 4)
hacha = Arma("Hacha", 4, 5)


thor = Superheroe("Thor", 20, 3, True, hacha)
hulk = Superheroe("Hulk", 20, 5, False, martillo)

print(f"Salud de Hulk: {hulk.salud}")
thor.atacar(hulk)
print(f"Salud de Hulk: {hulk.salud}")   
print(f"Resistencia del Hacha: {hacha.resistencia}")

thor.encontrar_mejora("Hacha")
print(f"Mejora encontrada. Resistencia del Hacha: {hacha.resistencia}")

thor.atacar(hulk)
print(f"Thor ataca a hulk. Salud de Hulk: {hulk.salud}")   
print(f"Resistencia del Hacha: {hacha.resistencia}")