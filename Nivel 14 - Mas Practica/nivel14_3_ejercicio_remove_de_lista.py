"""
Programa que elimine todos los meses que tengan la
letra "b"
"""
meses = ["enero", "febrero", "marzo", "abril",
         "mayo", "junio", "julio", "agosto",
         "septiembre", "octubre", "noviembre", "diciembre"]

nueva = []
# así no es posible, ya que al ir iterando, se va eliminando, por
# lo que tiene un elemento nuevo,
# saltando un elemento por cada uno que se elimina
# for mes in meses:
#     if "b" in mes:
#         meses.remove(mes)
# print(meses)

# se puede hacer también empezando por el último, para que
# el nº de items de la lista no varíe (usaremos índices):

# for i in range(len(meses) -1, -1, -1 ):  # iteramos desde el final
#     if "b" in meses[i]:
#         meses.remove(meses[i])
# print(meses)

# otra opción hubiera sido:
# for mes in meses:
#     if "b" not in mes:
#         nueva.append(mes)
# print(nueva)

# si lo que queremos es usar el método remove:

copia_meses = list(meses)
for mes in copia_meses:
    if "b" in mes:
        meses.remove(mes)
print(meses)


