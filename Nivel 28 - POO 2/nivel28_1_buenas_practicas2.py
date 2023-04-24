'''
Otro ejemplo de programación imperativo que podemos mejorar
con la POO:



class Termometro:
    
    def __init__(self, nombre, temperatura, limite):
        self.nombre = nombre
        self.temperatura = temperatura
        self.limite = limite
        
    def comprobar_temperatura(self, nueva_temperatura):
        self.temperatura = nueva_temperatura
        return self.temperatura
    
t = Termometro("Salón", 18, 21)

nueva_temperatura = t.comprobar_temperatura(17)

if nueva_temperatura > t.limite:
    print(f"Temperatura: {str(nueva_temperatura)}. Alarma")
else:
    print(f"Temperatura: {str(nueva_temperatura)}. Normal")
    
    
Con esto lo que estamos haciendo es sacar la lógica fuera de clase y accediendo
a sus atributos fuera de los métodos
    
    '''
    
# EN POO:

class Termometro:
    
    def __init__(self, nombre, temperatura, limite):
        self.nombre = nombre
        self.temperatura = temperatura
        self.limite = limite
        
    def comprobar_temperatura(self, nueva_temperatura):
        self.temperatura = nueva_temperatura
        if self.temperatura > self.limite:
            return f"Temperatura: {str(nueva_temperatura)}. Alarma"
        else:
            return f"Temperatura: {str(nueva_temperatura)}. Normal"
        
t = Termometro("Salón", 18, 21)

print(t.comprobar_temperatura(17))