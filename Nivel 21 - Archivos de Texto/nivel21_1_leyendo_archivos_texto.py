# primero hay que abrir el archivo, creando un objeto de
# tipo archivo, que nos permita el acceso al mismo

archivo = open("saludo.txt")  # si no se indica nada, se abre en modo lectura

# texto = archivo.read()  # tenemos el contenido del archivo
# print(texto)
# archivo.close()  # Siempre hay que cerrarlo a l final

# hay otros 2 métodos para leer archivos
# READLINES() --> Devuelve una lista con cada una de las líneas del texto

# lista = archivo.readlines()
# print(lista)  # -> ['Hola.\n', 'Que tal.\n', 'Encantado.\n', 'AdiÃ³s.']
# para quitar los saltos de linea:
# lista_formateada = []
# for elemento in lista:
#     linea = elemento.strip('\n')
#     lista_formateada.append(linea)
# print(lista_formateada)
# archivo.close()

# READLINE() --> Devuelve solo una de las líneas
# linea = archivo.readline()  # el puntero se coloca al final
# print(linea)
# linea = archivo.readline()  # siguiente línea después del puntero
# print(linea)
# archivo.close()
# con este método podemos usar un bucle para ir leyendo las líneas una por una

while True:
    linea = archivo.readline().strip()
    if linea == "":
        break
    else:
        print(linea)
archivo.close()