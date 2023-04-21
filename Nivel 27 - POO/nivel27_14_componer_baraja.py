'''
Componer una baraja francesa

Clase baraja compuesta por objetos tipo carta.

pica = "\u2660"
corazon = "\u2665"
diamante = "\u2666"
trebol = "\u2663"


class Carta:
    pass
    
class Baraja:
    pass
    
baraja = Baraja()
baraja.mostrar_baraja()

'''

pica = "\u2660"
corazon = "\u2665"
diamante = "\u2666"
trebol = "\u2663"

class Carta:
    
    def __init__(self, tanto, palo):
        self.tanto = tanto
        self.palo = palo
    
    def __str__(self): # como queremos que se muestre
        return f"[{self.tanto} - {self.palo}]"
    
    
class Baraja:
    
    def __init__(self):
        palos = ["\u2660", "\u2665", "\u2666", "\u2663"]
        tantos = ["A", "2", "3", "4", "5", "6", "7",
                  "8", "9", "X", "J", "Q", "K"]
        
        self.mazo = [] # lista vacía dnde guardaremos las cartas
        
        for t in tantos:
            for p in palos:
                carta = Carta(t, p)
                self.mazo.append(carta)

    def mostrar_baraja(self):
        print()
        for num, carta in enumerate(self.mazo):
            if (num-3) % 4 != 0:
                print(carta, end=" ") 
            else:
                print(carta)
        print()

    
baraja = Baraja()
baraja.mostrar_baraja()