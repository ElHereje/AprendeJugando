# CHOICE

# uso --> random.choice([op1, op2, op3,...])

# mejora el juego anterior con frases diferentes

import random

numero = random.randint(1, 100)
intentos = 0
jugando = True

op_alto = ["Uff...te has pasado.",
        "Demasiado alto...",
        "Vaya... muy alto...",
        "venga ya...no tan alto."]

op_bajo = ["Uff...te has quedado corto.",
        "Demasiado bajo...",
        "Vaya... muy bajo...",
        "venga ya...no tan bajo."]

while jugando:
    intentos += 1
    alto = random.choice(op_alto)
    bajo = random.choice(op_bajo)
    if intentos <= 7:
        elegido = int(input("Dime un nº del 1 al 100: "))
        if elegido == numero:
            print(f"ACERTASTES a la {intentos} vez...!!!!..enhorabuena crack...")
            jugando = False
        elif elegido > numero:
            print(f"{alto}\nLlevas {intentos} intentos")
        elif elegido < numero:
            print(f"{bajo}\nLlevas {intentos} intentos")
    else:
        print(f"Se te acabaron los intentos. EL numero era {numero}")

