
letras = ["E", "a", "i", "I", "A", "e"]

# para ordenarla alfabéticamente
letras.sort()
print(letras) # ['A', 'E', 'I', 'a', 'e', 'i'] es así por su valor UNICODE

# para hacerlo de un metodo clásico
letras = ["E", "a", "i", "I", "A", "e"]
letras.sort(key=str.lower)
print(letras) # ['a', 'A', 'E', 'e', 'i', 'I']

# ... con una func lambda:
letras = ["E", "a", "i", "I", "A", "e"]
letras.sort(key= lambda cadena: cadena.lower())
print(letras) # ['a', 'A', 'E', 'e', 'i', 'I']


'''
RETO:
ordenar de forma alfabética independientemente de may, acentos,...

palabras = ["isla", "último", "Ángela", "Italia",
            "índice", "Íñigo", "óptica", "árbol",
            "Úrsula", "época", "Olmedo", "Uruguay",
            "Elvira", "ukelele", "Argentina", "Écija",
            "Óscar", "amapola", "elefante", "objeto"]

'''