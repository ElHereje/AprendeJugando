"""
Método GET.
Simplifica la manera de acceso a un valor
"""

# telefonos = {"José": 1234,
#              "María": 3456,
#              "Andrés": 5678,
#              "Lucía": 9876}
#
#
# # como 2º argumento ponemos lo que queramos que aparezca si no existe
# print(telefonos.get("Pepe", "Esa clave no existe."))

inventario = {
    "Tornillos": 100,
    "Tuercas": 150,
    "Arandelas": 250
    }

articulo = input("Artículo: ")
num = inventario.get(articulo, 0)
print(f"{articulo}: {num}")
