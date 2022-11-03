# Convertir segundos dados en H, min y seg

segundos = int(input("Dime los segundos: "))

minutos = segundos // 60
segundos_resto = segundos % 60

horas = minutos // 60
minutos_restos = minutos % 60

print(f"{segundos} segundos son {horas} horas, {minutos_restos}, minutos y {segundos_resto} segundos")


# *************************


