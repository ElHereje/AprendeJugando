# pregunta al usuario si quiere seguir jugando

'''print("VAmos a jugar...")
resp = "s"

while resp == "s":
    print("Seguimos jugando")
    resp = input("Quieres seguir ??(S/N): ")

print("Fin del programa")'''


# programa que pida número entre 10 y 20.
# Si está dentro seguimos, si no, acaba.

numero = int(input("Introduce un nº entre 10 y 20: "))

while (numero >= 10) and (numero <= 20):
    print("Número dentro del intervalo.")
    numero = int(input("Introduce otro nº entre 10 y 20: "))
else:
    print(f"Número {numero} fuera de rango. Fin del programa")