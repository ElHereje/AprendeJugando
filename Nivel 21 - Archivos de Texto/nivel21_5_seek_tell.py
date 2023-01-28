"""
Vamos a ver los punteros que se generan al leer los archivos
read() permite argumentos, por ejemplo:
read(10) lee los 10 1ºs caracteres

tell() permite saber en que byte se encuentra el puntero
seek() nos permite posicionar el puntero
seek(0) --> ppio del archivo
seek(0, 2) --> final del archivo
"""

# archivo = open("alfabeto.txt", "r", encoding="utf-8")
# texto = archivo.read(10)
# print(archivo.tell())  # indica donde se encuentra el puntero
# print(texto)
# texto2 = archivo.read()
# print(texto2)
# archivo.seek(0)  # lo posicionamos en la posición 0
# texto3 = archivo.read()
# print(texto3)
# archivo.close()

archivo = open("eñe.txt", "r", encoding="utf-8")
archivo.seek(1) # ERROR --> el 1er byte se reserva para el tipo de codificación
texto = archivo.read()
print(texto)
archivo.close()



