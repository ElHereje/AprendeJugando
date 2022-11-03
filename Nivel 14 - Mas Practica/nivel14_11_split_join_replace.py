
# joins es lo contrario del método split (split separa según criterio,
# espacios por defecto)

# replace sustituye según criterio. Admite un 3er argumento, que indica
# las veces que reemplaza

# isalpha -> devuelve True (si todos los elementos son alfabéticos) o False

cad = "El sol sale por el este. Se pone por el oeste"

print(cad.split())
print(cad.split("."))

lista = cad.split()
print(" ".join(lista))  # --> El sol sale por el este. Se pone por el oeste
print("".join(lista))  # --> Elsolsaleporeleste.Seponeporeloeste
print("-".join(lista))  # --> El-sol-sale-por-el-este.-Se-pone-por-el-oeste

cade = "-".join(lista)
cade2 = cade.replace("-", " ")  # -> sustituye guion por espacio
print(cade2)  # -> El sol sale por el este. Se pone por el oeste
cade3 = cade.replace("-", " ", 2) # sustituye solo los 2 primeros
print(cade3)  # -> El sol sale-por-el-este.-Se-pone-por-el-oeste
