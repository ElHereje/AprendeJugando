"""
Programa que borre los elementos repetidos de una lista
"""

num = [1, 2, 3, 2, 5, 3, 4, 6, 5, 7, 8]

nueva = []

# una manera fácil sería.....
# for i in range(len(num)):
#     if num[i] not in num_copy:
#         num_copy.append(num[i])
# print(num_copy)


# pero si queremos usar el método remove:
#  creamos otra lista adicional, copia de la original:

num_copy = list(num)
for n in num_copy:
    if n not in nueva: #  si no está en nueva, que lo copia a ella
        nueva.append(n)
    else: # si ya está, es que es repetido, por lo que la eliminamos de la lista original
        num.remove(n)
print(nueva)
print(num)


