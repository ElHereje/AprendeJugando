"""
Inventario de las letras y su cantidad que se guardan en una
cajonera con 2 cajones
"""
# [POSICIÓN, LETRA, CANTIDAD, [COLUMNA, FILA]]
cajonera = [["Arriba", "A", 10, [1, 1]],
            ["Arriba", "B", 15, [2, 1]],
            ["Arriba", "C", 17, [3, 1]],
            ["Arriba", "D", 19, [4, 1]],
            ["Arriba", "E", 10, [5, 1]],
            ["Arriba", "F", 8, [1, 2]],
            ["Arriba", "G", 21, [2, 2]],
            ["Arriba", "H", 24, [3, 2]],
            ["Arriba", "I", 14, [4, 2]],
            ["Arriba", "J", 9, [5, 2]],
            ["Arriba", "K", 34, [1, 3]],
            ["Arriba", "L", 23, [2, 3]],
            ["Arriba", "M", 45, [3, 3]],
            ["Arriba", "N", 16, [4, 3]],
            ["Arriba", "Ñ", 19, [5, 3]],
            ["Abajo", "O", 8, [1, 1]],
            ["Abajo", "P", 21, [2, 1]],
            ["Abajo", "Q", 12, [3, 1]],
            ["Abajo", "R", 10, [4, 1]],
            ["Abajo", "S", 18, [5, 1]],
            ["Abajo", "T", 31, [1, 2]],
            ["Abajo", "U", 10, [2, 2]],
            ["Abajo", "V", 14, [3, 2]],
            ["Abajo", "W", 17, [4, 2]],
            ["Abajo", "X", 13, [5, 2]],
            ["Abajo", "Y", 2, [1, 3]],
            ["Abajo", "Z", 23, [2, 3]]
            ]

for i in cajonera:
    print(f"Letra: {i[1]}, Cajón de {i[0]}. Cantidad: {i[2]}. Posición {i[3]}")