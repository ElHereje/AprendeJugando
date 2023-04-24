'''
# ESTILO DE PROGRAMACION IMPERATIVA

class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.amigos = []
        
        
javier = Persona("Javier", 17)

if javier.edad >= 18:
    print(f"{javier.nombre} es mayor de edad")
else:
    print(f"{javier.nombre} es menor de edad")
    
    
Con esto, lo que hacemos es sacer la lógica del programa fuera de la clase, 
colocándola en el fujod el programa 

'''

# EN LA POO SE HARÍA PODEMOS ENCAPSULAR TODA LA LÓGICA DEL PROGRAMA
# EN UN MÉTODO:

class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.amigos = []
        
    def verificar_edad(self, mayoria_edad):
        if self.edad >= mayoria_edad:
            return f"{self.nombre} es mayor de edad"
        else:
            return f"{self.nombre} es menor de edad"
        
javier = Persona("Javier", 17)

print(javier.verificar_edad(18))