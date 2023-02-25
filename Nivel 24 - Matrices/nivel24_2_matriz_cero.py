'''
Crea una matriz cero de orden 10x15 de forma automática
'''

# mc = [[0] * 15] * 10

# for fila in mc:
#     print(fila)
    
# esta no está bién hecho, ya que no hemos concatenados 10 listas,
# sino una sola lista 
# para crear 10 listas:

mc = []

# for i in range(10):
#     mc.append([0] * 15)

# otra manera:
for i in range(10):
    mc.append([])
    for j in range(15):
        mc[i].append(0)

# for fila in mc:
#     print(fila)
    
# para ver si está bién construida:

mc[2][3] = 2  # fila 3, coulmna 4 

for fila in mc:
    print(fila)