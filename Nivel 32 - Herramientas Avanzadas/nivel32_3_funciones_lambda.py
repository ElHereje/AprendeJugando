'''
Son funciones anónimas.
se representan por:

lambda "parametros" : "expresion"

'''

# funcion que defina la cuarta parte de un nº que le pasemos, por ejemplo, 17:
print((lambda x: x/4), (17))

# tambien podríamos haberla definido, pero no es lo normal:
cuarta = lambda x: x/4
print(cuarta(17))

#  para ordenar una lista...según orden alfabéico
datos = [[9, "Jc", 2],
         [7, "aK", 5],
         [4, "Sv", 6],
         [3, "Dw", 5],
         [5, "mx", 4]]

datos.sort(key=lambda x: x[1])
print(datos) # [[3, 'Dw', 5], [9, 'Jc', 2], [4, 'Sv', 6], [7, 'aK', 5], [5, 'mx', 4]]

# independiente de las may.
datos = [[9, "Jc", 2],
         [7, "aK", 5],
         [4, "Sv", 6],
         [3, "Dw", 5],
         [5, "mx", 4]]
datos.sort(key=lambda x: x[1].lower())
print(datos)  # [[7, 'aK', 5], [3, 'Dw', 5], [9, 'Jc', 2], [5, 'mx', 4], [4, 'Sv', 6]]

# ...según la suma de sus datos numéricos:
datos = [[9, "Jc", 2],
         [7, "aK", 5],
         [4, "Sv", 6],
         [3, "Dw", 5],
         [5, "mx", 4]]
datos.sort(key=lambda x: x[0] + x[2])
print(datos) # [[3, 'Dw', 5], [5, 'mx', 4], [4, 'Sv', 6], [9, 'Jc', 2], [7, 'aK', 5]]