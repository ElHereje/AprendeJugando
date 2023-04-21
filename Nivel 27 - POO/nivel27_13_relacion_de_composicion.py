'''
Vamos a hacer un dibujo de estrellas (composicion)
la llamada a una clase se realizará dentro de la otra
'''

import random

class Estrella:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.forma = random.choice(["*", ".", ".", "."])
        
    def __str__(self):
        return self.forma # para que se muestre la forma
    

class Cielo:
    
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.cielo = [] #lista anidada
        # creamos una lista con i listas anidadas
        for i in range(filas):
            self.cielo.append([])
            # por cada lista anidada, tenemos tantos 
            # espacios vacios como columnas indiquemos
            for j in range(columnas):
                self.cielo[i].append(" ")
                
    def poner_estrellas(self, numero_estrellas):
        for i in range(numero_estrellas):
            x = random.randint(0, self.columnas-1)
            y = random.randint(0, self.filas-1)
            # creamos el objeto estrella dentro de la clase cielo
            estrella = Estrella(x, y)
            # una vez creado, lo colocamos en el cielo
            self.cielo[y][x] = estrella
            
    # para mostrar el cielo.
    def mostrar(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                print(self.cielo[i][j], end="")
            print()
            

import os

os.system("cls")

cielo_1 = Cielo(18, 60)
cielo_1.poner_estrellas(150)
cielo_1.mostrar()