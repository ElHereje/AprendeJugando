# TUPLAS

# Las tuplas siempre van entre paréntesis
# NO SE PUEDEN MODIFICAR

'''t1 = (1, 2, 3)
t2 = (4, 5, 6)

t3 = t1 + t2
print(t3)
t4 = t2 + t1
print(t4)
print(t4[2])
print(t4[2:3])
print(len(t4 ))'''

'''
Las tuplas con un solo elemento se representan --> (4,)
mi_tupla = (1, 2, 3)
mi_tupla2 = mi_tupla + (4,)
print(mi_tupla2) # --> (1, 2, 3, 4)  
mi_tupla2 += (5, 6)
print(mi_tupla2) # --> (1, 2, 3, 4, 5, 6) 

'''

# Tenemos 3 tuplas:
# Crea otra a partir de ellas que contenga las mascotas

mamiferos = ("tigre", "gato", "león")
aves = ("aguila", "buitre", "canario")
reptiles = ("tortuga", "serpiente")

mascotas = (mamiferos[1], aves[2], reptiles[0])
mascotas_b = mamiferos[1:2] + aves[2:] + reptiles[0:1]
mascotas_c = (mamiferos[1],) + (aves[2],) + (reptiles[0],)
print(mascotas)
print(mascotas_b)
print(mascotas_c)
