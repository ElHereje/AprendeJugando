from caballo import Caballo
import random

class Hipodromo:
    
    def __init__(self, nombre, filas, metros, ornamento):
        self.nombre = nombre
        self.filas = filas
        self.metros = metros
        self.ornamento = ornamento
        self.pista = [] # será una lista anidada con x filas e y metros
        for i in range(filas):
            self.pista.append([ornamento] * metros)
        self.caballos=[]
        # Llamamos al método traer caballos para crearlos en el constructor
        self.traer_caballos()

    def traer_caballos(self):
        nombres = ["r", "s", "t", "p", "n", "k", "w", "y", "f", "z"]
        for i in range(self.filas):
            favorito = random.choice([True, False])
            caballo = Caballo(nombres[i], favorito)
            self.caballos.append(caballo)
            
    def avanzar_caballos(self):
        for caballo in self.caballos:
            caballo.avanzar()

    def poner_caballos(self):
        for i in range(self.filas):
            self.pista[i][self.caballos[i].metro] = self.caballos[i]

    def poner_ornamento(self):
        for i in range(self.filas):
            self.pista[i][self.caballos[i].metro] = self.ornamento

    def mostrar_favoritos(self):
        print()
        print(" Los caballos favoritos de hoy son: ", end=" ")
        for caballo in self.caballos:
            print(caballo, end=" ")
        print()
        
    def comprobar_ganadores(self):
        ganadores = []
        for caballo in self.caballos:
            if caballo.metro > self.metros - 7:
                ganadores.append(caballo)
        return ganadores
        
    def mostrar(self):
        print()
        print(f"    HIPÓDROMO DE {self.nombre}".center(self.metros))
        print()
        print
        print("  ||SALIDA" + ("=" * ((self.metros)-14)) + "META||")
        print()
        for i in range(self.filas):
            print(" ", end=" ")
            for j in range(self.metros):
                print(self.pista[i][j], end="") # veremos el ornamento o el caballo...
            print()