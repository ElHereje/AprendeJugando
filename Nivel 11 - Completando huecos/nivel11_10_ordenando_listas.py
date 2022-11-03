# SE PUEDE ORDENAR CON UN ALGORITMO O CON UN MÉTODO o una función


edades = [12, 18, 42, 21, 24, 13, 21, 35, 17, 23]

# podemos hacerlo con el método sort.
# este MÉTODO NO DEVUELVE NADA

edades.sort() # así perdemos la lista original
print(edades)

# para ordenarla a la inversa
edades.sort(reverse=True)
print(edades)

# para no perder la original, usamos la función sorted
# esta FUNCIÓN DEVUELVE UNA LISTA ORDENADA

edades = [12, 18, 42, 21, 24, 13, 21, 35, 17, 23]
edades_ordenadas = sorted(edades)
edades_inversa = sorted(edades, reverse=True)
print()
print(edades)
print(edades_ordenadas)
print(edades_inversa)
