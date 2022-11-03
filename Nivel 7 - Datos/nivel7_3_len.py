'''
Comprobar cuántas veces aparece el caracter 'o', con o sin tilde,
de la siguiente cadea de caracteres.
'''

cadena = '''Muchos años después, frente al pelotón de 
fusilamiento, el coronel Aureliano Buendía había de 
recordar aquella tarde remota en que su padre lo llevó
a conocer el hielo.'''

cantidad = 0
contador = 0

while contador < len(cadena):
    if cadena[contador] == "o" or cadena[contador] == "ó":
        cantidad += 1
    contador += 1
print(f"La letra 'o' aparece {cantidad} veces")