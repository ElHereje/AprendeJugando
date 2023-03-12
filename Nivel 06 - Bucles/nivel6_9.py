# Pregunta un número del 1 al 5 y luego una vocal.
# Tienes 100 puntos, si aciertas uno te quita 2 y si no te quita 5.
# No se acaba hasta que aciertes los dos.
# Cuando el programa acaba, te dice los puntos que te quedan.

vocal = "e"
numero = "6"
puntos = 100
print("ADIVINA NÚMERO Y LETRA\n")
print("Tienes 100 puntos.")
acertado = False  # <-- esta es la bandera
while not acertado:
    intento_vocal = input("Introduce Vocal: ")
    intento_numero = input("Introduce un nº de 1 al 5: ")
    if (numero != intento_numero) and (intento_vocal != vocal):
        print("Ambos datos Incorrectos. 5 puntos menos\n")
        puntos -= 5
        print(f"Tienes {puntos} puntos\n")
    elif (numero != intento_numero) or (intento_vocal != vocal):
        print("Un campo incorrecto. 2 puntos menos\n")
        puntos -= 2
        print(f"Tienes {puntos} puntos")
    else:
        acertado = True
        print("Datos Acertados")
        print(f"Te han quedado {puntos} puntos")

print("Fin del Juego")