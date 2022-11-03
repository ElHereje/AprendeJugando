"""
Cinco amigos van a hacer una carrera:
"Tomás", "María", "Laura", "Miguel", "Carlos"
Muestra todos los posibles resultados que se pueden dar,
es decir, el orden en que pueden llegar a la meta los cinco amigos.
Incluye un contador que comprueba cuantas posibilidades hay.

Serían permutaciones sin repetición --> fórmula : m!
5*4*3*2*1 = 120 posibles resultados

"""

corredores = ["Tomás", "María", "Laura", "Miguel", "Carlos"]

contador = 0

# Primero ponemos los for que incluyan a todos:
for i in corredores:
    for j in corredores:
        for k in corredores:
            for l in corredores:
                for m in corredores:
                    # luego confirmamos que no se repitan:
                    if (i != j and i != k and i != l and i != m and
                            j != k and j != l and j != m and
                            k != l and k != m and l != m):
                        # creamos la posible lista
                        orden = [i, j, k, l, m]
                        # aumentamos el contador
                        contador += 1
                        # imprimimos la posibilidad
                        print(f"Posibilidad {contador:<3d} : {orden}")
