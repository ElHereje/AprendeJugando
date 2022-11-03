'''
Programa que te pida que introduzcas productos y crea
una lista de la compra con esos productos, que se muestra al final
'''

'''compra = []

while True:
    articulo = input("Introduce artículo. Para finalizar escribe 'fin': ")
    if articulo.lower() == "fin":
        break
    else:
        compra.append(articulo)
print(compra)

# Si queremos aumentar la lista con otra diferente, usamos 'extend'

compra2 = ["leche", "azucar"]

compra.extend(compra2)
print(compra)'''


'''Crea una lista con los números enteros del 1 al 5 a partir de los datos
que se dan.
Usa append o extend, según convenga'''


# 1
n_a = [1, 2, 3]
m_a = [4, 5]

# 2
n_b = [1, 2, 3, 4]
m_b = [5]

n_a.extend(m_a)
# n_b.append(m_b) # --> NOO  ..esto añade la lista como un elemento
#                       y no un elemento de la lista
n_b.extend(m_b)
print(n_a)
print(n_b)


