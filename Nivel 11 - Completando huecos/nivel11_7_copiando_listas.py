"""
1. Crea una lista vacía llamada "letras" (usando una función)
2. Añade la letra "a" a esa lista (usando un método)
3. Haz una copia de la lista (creando una lista distinta)
4. Añade la letra "b" a la copia.
5. Comprueba los elementos de ambas listas
"""

letras = list()
letras.append("a")
copia = list(letras)
copia.append("b")
print(letras, copia)  # --> ['a'] ['a', 'b']

