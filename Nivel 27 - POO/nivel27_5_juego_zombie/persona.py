class Persona:
    
    # inicializamos los objetos de la clase
    # self hace referencia a cada uno de los objetos
    # Agregamos el atributo "energía"
     
    def __init__(self, nombre):
        self.nombre = nombre
        self.calle = 1
        self.energia = 15
        
        
    # modificamos el método para incluir el nuevo atributo
    # y la forma de devolver los datos
    def situacion(self):
        return self.nombre, self.calle, self.energia
    
    
    # eliminamos ahora una unidad de energía por cada movimiento
    def moverse(self, velocidad):
        if velocidad == "1":
            self.calle += 1
        elif velocidad == "2":
            self.calle += 2
        else:
            self.calle += 3 
        self.energia -= 1
