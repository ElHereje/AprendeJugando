# veremos % y format

producto = "patatas"
precio = 5
datos = {"producto": "patatas", "precio": 5}

# con %
print("Precio de %s es %10f.2€" %(producto, precio))
print()
print("Precio de %(producto)s es %(precio)s euros" % datos)

# con format
print("Precio de {} es {:10.2f}€".format(producto, precio))
print("Precio de {n} es {p:10.2f}€".format(n=producto, p=precio))
print("Precio de {} es {:<10.2f}€".format(producto, precio))
print("Precio de {} es {:>10.2f}€".format(producto, precio))
print("Precio de {} es {:^10.2f}€".format(producto, precio))
print()
print("Precio de {d[producto]} es {d[precio]} euros".format(d=datos))
print()
print("Precio de {n} es {p} euros".format(n=datos['producto'], p=datos['precio']))
print()
print(f"Precio de {producto} es {precio} euros".format(**datos))
