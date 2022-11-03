# GUARDANDO ELEMENTOS

"""
Tenemos una tupla con los meses del año. Queremos saber
qué meses tienen la letra "b" en su nombre
"""
meses = ("Enero", "Febrero", "Marzo", "Abril",
         "Mayo", "Junio", "Julio", "Agosto",
         "Septiembre", "Octubre", "Noviembre", "Diciembre")

selec = ()

for mes in meses:
    if "b" in mes:
        selec += (mes,)

print(f"Los meses que contiene la letra B son:\n{selec}")