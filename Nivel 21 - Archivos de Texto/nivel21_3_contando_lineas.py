"""
Contar las líneas del archivo quijote.txt
"""

archivo = open("quijote.txt","r", encoding="utf-8")

# con readlines()
# lineas = archivo.readlines()
# print(len(lineas))

# con read() --> contando los saltos de línea
# lineas = archivo.read()
# n = 0
# for i in lineas: # i es cada caracter en el texto
#     if i == "\n":
#         n += 1
# print(n)

# con readline() devuelve una sola línea
# n = 0
# while True:
#     if archivo.readline() != "":
#         n += 1
#     else:
#         break
# print(n)
#


# sin usar métodos  --> ES LA MÁS SENCILLA Y DIRECTA
n = 0
for linea in archivo:
    n += 1
print(n)

# archivo.close()