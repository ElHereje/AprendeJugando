# VAMOS A VER LOS MÉTODOS PROPIOS DE LAS LISTAS
# mutables significa que podemos cambiar un valor sin tener que crear una nueva lista

# el tipo entero es inmutable. Cuando se crear se guarda en una única dirección
n = 1
print(id(n))  # 1800320280880 --> es la dirección de memoria donde está guardado n

# si se modifica n, lo que se hace es guardarse en otra dirección
n = 2
print(id(n))  # --> 1800320280912

# ESTO NO OCURRE CO LAS LISTAS:

numeros = [1, 2, 3]
print(id(numeros))  # --> 2043073677312
# si la modificamos:
numeros[0] = 4
print(id(numeros))  # --> 2043073677312  SIGUE SIENDO LA MISMA LOCALIZACIÓN

numeros = numeros + [5]
print(id(numeros))  # --> 2043077503872 Si añadimos un valor, entonces si cambia de identidad

# HAY MÉTODOS QUE EVITAN ESTO Y SON MAS EFICACES

numeros.append(3)
print(id(numeros))  # --> 2043077503872 Este método no crea otra, sino que la modifica



