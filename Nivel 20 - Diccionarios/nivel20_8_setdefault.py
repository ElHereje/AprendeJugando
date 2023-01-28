
'''
setdafault añade al diccionario un elemento
'''

materiales = {
    "cuadernos": 5,
    "bolígrafos": 7,
    "reglas": 3,
    "gomas": 4
}

# articulo = input("Artículo: ")
# unidades = materiales.get(articulo, 0)  # si no hay, muestra 0
# print(f"Hay {unidades} unidades de {articulo}")

# queremos que cuando el artículo no esté, lo incluya con las cantidades indicadas

articulo = input("Artículo: ")
unidades = materiales.setdefault(articulo, 0)  # si no hay, muestra 0
print(f"Hay {unidades} unidades de {articulo}")

# por ejemplo, si cogemos el programa del video anterior...
frase = "Hoy ha salido el sol y hace una mañana estupenda"
conteo = {}
# for letra in frase.lower():
#     if letra not in conteo:
#         conteo[letra] = 1
#     else:
#         conteo[letra] += 1
# for k, v in conteo.items():
#     print(f"Letra {k}: {v} veces")
# esto lo podríamos haber resumido como...
for letra in frase.lower():
    conteo.setdefault(letra, 0)
    conteo[letra] += 1
for k, v in conteo.items():
    print(f"Letra {k}: {v} veces")
