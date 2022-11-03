# F-String

producto = "patatas"
productos = ["patatas", "arroz", "zanahorias", "tomates"]
precio = 5
precios = [10, 200, 3, 4000]
precio2 = 5.123
descuento = 2

datos = {"prod": "patatas", "prec": 5}

# simples
print(f"El precio de las {producto} es de {precio}€")
print(f"El precio de {producto} es de {precio:10.2f}€")
print(f"El precio de las {producto} es de {precio - descuento}€")
print(f"El precio de las {producto.capitalize()} es de {precio - descuento}€")
print()

# listas
for i in range(len(productos)):
    print(f"El precio de {productos[i]:15} es de {precios[i]:10d}€")
print()

# diccionarios
print(f"Precio de {datos['prod']} es de {datos['prec']}€")
