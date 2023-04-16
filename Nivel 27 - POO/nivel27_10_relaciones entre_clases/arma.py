class Arma:
    
    def __init__(self, nombre, resistencia, destruccion, cat=1):
        self.nombre = nombre
        self.resistencia = resistencia
        self.destruccion = destruccion
        self.cat = cat
        
    def __str__(self):
        return self.nombre