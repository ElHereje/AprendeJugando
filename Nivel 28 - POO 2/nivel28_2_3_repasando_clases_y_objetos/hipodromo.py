class Hipodromo:
    
    def __init__(self, nombre, filas, metros, ornamento):
        self.nombre = nombre
        self.filas = filas
        self.metros = metros
        self.ornamento = ornamento
        self.pista = [] # será una lista anidada con x filas e y metros
        for i in range(filas):
            self.pista.append([ornamento] * metros)
            
    # como lo hacemos por agregación...
    def poner_caballo(self, caballo, fila, metro):
        self.pista[fila][metro] = caballo
        
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