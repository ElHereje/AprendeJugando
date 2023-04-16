'''
Unos de las características esenciales del paradigma de la POO es que los 
objetos se pueden pasar mensajes unos a otros a através de métodos.
Este es un concepto esencial


Por ejemplo.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return self.nombre
        
         
    # hasta ahora, si queremos que se presente:
    def presentarse(self):
        print(f"Me llamo {}. ¿Como te llamas tú?...)     

jorge = Persona("Jorge", 24)
maria = Persona("Maria", 23)

'''

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return self.nombre
        
         
    # hasta ahora, si queremos que se presente:
    def presentarse(self):
        print(f"Me llamo {self}. ¿Como te llamas tú?...")  
        
    # con la POO podemos hacer:
    
    def responder(self, otro): # otro actua como referencia a un objeto a pasar
        print(f"Hola {otro.nombre}, me llamo {self.nombre}")
        
    def pregunta_edad(self, otro):
        print(f"Hola {otro.nombre}, ¿Cuantos años tienes?")
        
    def responde_edad(self, otro):
        print(f"Hola {otro.nombre}, tengo {self.edad} años")

jorge = Persona("Jorge", 24)
maria = Persona("Maria", 23)

jorge.presentarse() # Me llamo Jorge. ¿Como te llamas tú?...
maria.presentarse() # Me llamo Maria. ¿Como te llamas tú?...

maria.responder(jorge) # Hola Jorge, me llamo Maria
jorge.responder(maria) # Hola Maria, me llamo Jorge

maria.pregunta_edad(jorge) # Hola Jorge, ¿Cuantos años tienes?
jorge.responde_edad(maria) # Hola Maria, tengo 24 años