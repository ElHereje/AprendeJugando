# ITERACIÓN POR LISTAS

letras = ["f", "g", "h", "j", "l", "m", "p", "s"]

# comprobar si está una letra con IF
'''letra = input("Introduce una letra: ")
if letra in letras:
    print(f"La letra {letra} si está en la lista")
else:
    if "m" in letras:
        print(f"La letra {letra} NO está en la lista")'''


# *****************************************************************


# comprobar si está una letra con FOR
'''letra = input("Introduce una letra: ")
for i in letras:
    if i == letra:
        print(f"La letra {letra} está en la lista")
    else:
        print(f"La letra {letra} NO está en la lista")'''

# *****************************************************************


# para que solo muestre el resultado si está o no
'''encontrado = False
letra = input("Introduce una letra: ")
for i in letras:
    if i == letra:
        encontrado = True

if encontrado:
    print(f"La letra '{letra}' SI está en la lista")
else:
    print(f"La letra '{letra}' NO está en la lista")'''


# ****************************************************************


'''
Programa que pide un número. Si ese nº, más alguno de la
lista da 100, el programa dice que se cumple la condición
'''

lista = [28, 36, 43, 52, 61, 75, 84, 97]
num = int(input("Dime un nº: "))
se_cumple = False
for i in lista:
    if (num + i) == 100:
        se_cumple = True
if se_cumple:
    print("Se cumple")
else:
    print("No se cumple")
