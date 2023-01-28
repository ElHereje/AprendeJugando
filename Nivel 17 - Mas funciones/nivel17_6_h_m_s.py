"""
Programa con una función que convierta segundos en horas,
minutos y segundos.
Pide los segundos y muestra el resultado.

En el nivel 5_3 se hizo....

segundos = int(input("Dime los segundos: "))
minutos = segundos // 60
segundos_resto = segundos % 60
horas = minutos // 60
minutos_restos = minutos % 60
print(f"{segundos} segundos son {horas} horas, {minutos_restos}, minutos y {segundos_resto} segundos")

"""
def h_m_s(segundos):
    minutos = segundos // 60   # división sin resto
    segundos_resto = segundos % 60
    horas = minutos // 60   # división sin resto
    minutos_restos = minutos % 60
    return horas, minutos_restos, segundos_resto


#  otra manera mas compacta:
def h_m_s_V2(segundos):
    horas = segundos // 60 // 60
    minutos = segundos // 60 % 60
    segundos = segundos % 60
    return horas, minutos, segundos

cantidad = int(input("Dime los segundos: "))
h, m, s = h_m_s_V2(cantidad)
print(f"{cantidad} segundos son {h} horas, {m}, minutos y {s} segundos")
