# buscar todos los números capicúas entre otros dos dados

inicial = 10000
final = 12000

capicuas= []

for numero in range(inicial, final):
    # primero hay que convertir los números en cadenas
    cadena = str(numero)
    reverso = cadena[::-1]
    if reverso == cadena:
        capicuas.append(numero)
print(capicuas)
