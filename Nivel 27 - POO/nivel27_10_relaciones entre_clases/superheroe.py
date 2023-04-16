

class Superheroe:
    
    def __init__(self, nombre, salud, ataque, escudo, arma):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque
        self.escudo = escudo
        self.arma = arma
        
    def __str__(self):  
        return self.nombre
    
    def atacar(self, otro):
        otro.salud -= self.ataque + self.arma.destruccion
        self.arma.resistencia -= 1