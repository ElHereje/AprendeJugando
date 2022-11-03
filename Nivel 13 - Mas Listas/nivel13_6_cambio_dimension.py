"""
Pasar una lista bidimensional a 2 listas unidimensionales,
y viceversa.
"""

grupos = [[1, "A"], [2, "B"], [3, "C"], [4, "D"], [5, "E"],
          [6, "F"], [7, "G"], [8, "H"], [9, "I"], [0, "J"]]

# num = list()
# letras = list()
# for g in range(len(grupos)):
#     num.append(grupos[g][0])
#     letras.append(grupos[g][1])
# ahora pasamos las unidimensionales a una bidimensional:
# grupos2 = list()
# for n in range(len(num)):
#     grupos2.append([num[n], letras[n]])
# print(grupos2)

# otra manera:
num = []
letras = []
for lista in grupos:
    num.append(lista[0])
    letras.append(lista[1])


print()
print("Unidimensionales: ".center(50))
print(num)
print(letras)
print()
print("Bidimensional: ".center(50))

# ahora pasamos las unidimensionales a una bidimensional:
grupos2 = list()
for n in range(len(num)):
    grupos2.append([num[n], letras[n]])
print(grupos2)



