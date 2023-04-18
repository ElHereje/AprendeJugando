class Arma:
    
    def __init__(self, nombre, resistencia, destruccion, cat=1):
        self.nombre = nombre
        self.resistencia = resistencia
        self.destruccion = destruccion
        self.cat = cat
        
    def __str__(self):
        return self.nombre
    
    # creamos un método que aumente la cat del arma
    def elevar_categoria(self):
        self.cat += 1
        self.resistencia += 2
        self.destruccion += 1