'''

DEFINIR EL MÉTODO ATACAR TAL QUE:

class Superheroe:
    
    def __init__(self, nombre, salud, ataque, escudo):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque
        self.escudo = escudo
        
    def atacar():
        
        Si el enemigo no tiene puesto el escudo su salud disminuye
        la cantidad de ataque, si lo tiene puesto la salud del que
        ataca disminuye la cantidad del ataque.
        Poner prints para mostrar los efectos del ataque tanto en el 
        superheroe que ataa como en el otro
        
        pass
    
    
thor = Superheroe("Thor", 20, 3, True)
hulk = Superheroe("Hulk", 20, 5, False)

thor.atacar(hulk)   # Salud de hulk: 20-3. Salud de thor: Igual
hulk.atacar(thor)   # Salud de thor: igual. Salud de hulk: 17-5

'''