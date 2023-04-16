
from superheroe import Superheroe
from arma import Arma

martillo = Arma("Martillo", 6, 4)
hacha = Arma("Hacha", 4, 5)


thor = Superheroe("Thor", 20, 3, True, martillo)
hulk = Superheroe("Hulk", 20, 5, False, hacha)

print(f"Salud de Hulk: {hulk.salud}")
thor.atacar(hulk)
print(f"Salud de Hulk: {hulk.salud}")   