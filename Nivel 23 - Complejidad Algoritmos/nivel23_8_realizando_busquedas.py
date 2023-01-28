'''
vamos a crear un censo de población, con opciones de búsqueda. Usaremos dos
funciones (POR NOMBRE Y POR NUMERO) definiendo el algoritmo mas adecuado para
cada una.

'''

import random

censo = []
alfabeto = "ABDEFGIJAEIOULMNOPRSTUAEIOU"
numero = 0

print("creando censo...")

for i in range(500_000):
    
    aumento = random.randint(1, 2)
    numero += aumento
    
    letras = random.sample(alfabeto, 5)
    nombre = "".join(letras)
    
    edad = random.randint(18, 99)
    
    impuestos = random.choice((True, True, True, False)) # pagados o no
    
    censo.append([numero, nombre, edad, impuestos])
    
    if len(censo) % 100_000 == 0: # comprobamos como se crean cada 100000 registros
        print("Creados", len(censo), "registros")
        
print("Censo creado.")
print("Ultimo registro: ", censo[-1])

def busqueda_numero(lista, elemento):
    
    '''Busca registros por nº. Búsqueda binaria.'''
    
    inicio = 0
    final = len(lista) - 1
    
    while inicio <= final:
        
        medio = (inicio + final) // 2
        if lista[medio][0] == elemento: # hacemos referencia l nº que está en el indice 0 de cada registro
            return lista[medio]
        elif lista[medio][0] < elemento:
            inicio = medio + 1  # adelantamos el inicio
        elif lista[medio][0] > elemento:
            final = medio - 1  # adelantamos el final
    return None


def busqueda_nombre(lista, elemento):
    
    '''Busca registro por nombre. Búsqueda lineal.'''
    
    encontrados = []  # por si el nombre está repetido
    
    for registro in lista:
        if registro[1] == elemento:
            encontrados.append(registro)
    if len(encontrados) == 0:
        return None
    else: 
        return encontrados


def muestra_registro(registro):
    
    if registro == None:
        print("No existen registros con ese dato.")
    else:
        print("------------------------")
        print(f"Número: {registro[0]}")
        print(f"Nombre: {registro[1]}")
        print(f"Edad: {registro[2]}")
        print(f"Impuestos: {registro[3]}")
        
        
def menu():
    
    print("----------------------")
    print("- Censo de Población -")
    print("----------------------")
    print("1. Buscar por número.")
    print("2. Buscar por nombre.")
    print("3. Salir.")
    print()
    opcion = ""
    while opcion not in ("1", "2", "3"):
        opcion = input("--> ")
    return opcion


while True:
    
    op = menu()
    
    if op == "1":
        try:
            numero = int(input("Introduce número: "))
        except ValueError:
            print("Introduce un nº entero")
        else:
            registro = busqueda_numero(censo, numero)
            muestra_registro(registro)
            
    elif op == "2":
        nombre = input("Introduce nombre: ").upper()
        registros = busqueda_nombre(censo, nombre)
        if registros == None:
            print("No existen registros con ese dato.")
        else:
            for registro in registros:
                muestra_registro(registro)
                
    elif op == "3":
        break