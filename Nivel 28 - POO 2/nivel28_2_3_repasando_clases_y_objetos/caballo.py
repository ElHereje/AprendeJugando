import random

class Caballo:
    
    def __init__(self, nombre, favorito=False):
        self.nombre = nombre
        self.favorito = favorito
        self.metro = 0 # posición donde se encuentra
        
    def __str__(self):
        return self.nombre
    
    def avanzar(self):
        if self.favorito:
            self.metro += random.randint(1, 6)
        else:
            self.metro += random.randint(1, 5)      
            
            