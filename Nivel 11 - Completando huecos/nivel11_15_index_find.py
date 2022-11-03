"""
Estos métodos pertenecen a las listas y cadenas de caracteres
"""

palabra = "zanahoria"

indice_h = palabra.find("h")
print(indice_h)  # --> 4
print()
# si lo que se busca no se encuentra, devuelve un -1

indice_j = palabra.find("j")
print(indice_j)  # --> -1
print()

# el método index es muy parecido, pero si no se encuentra
# muestra un error
indice_h = palabra.find("h")
print(indice_h)  # --> 4
'''indice_k = palabra.index("k")
print(indice_k)  # error'''
print()

#  en este caso usamos in if para prevenir el error
if "k" in palabra:
    indice_k = palabra.index("k")
else:
    print("No existe")

# EN LAS LISTAS SOLO ESTÁ EL MÉTODO INDEX.
# va a dar el índice de la primera ocurrencia

lista = ["a", "b", "c", "d", "a", "c", "b"]
if "c" in lista:
    print(lista.index("c"))
else:
    print("No existe")

# podemos indicar rango de posición:
if "a" in lista[3:]:  # busca desde la posición 3 hasta el final
    print(lista.index("a", 3))
else:
    print("No existe")
print()

print(palabra.find("a", 4))  # -> busca desde la posición 4
