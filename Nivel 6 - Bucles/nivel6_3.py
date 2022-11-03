# Igual que el anterior pero con un contador

print("Vamos a jugar...")
resp = "s"
contador = 0
while resp == "s":
    print("Seguimos jugando")
    resp = input("Quieres seguir ??(S/N): ")
    contador += 1

print("Fin del programa")
print(f"Número de veces que itera el bucle: {contador}")