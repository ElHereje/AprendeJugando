#  las copias de listas anidadas se pueden hacer de manera manual
#  de la siguiente manera:

p = [1, [2, 3], [4, 5, 6]]
q = []

for i in p:
    q.append(i)
print(q)

# también se podría hacer con list de la siguiente manera:

q2 = [p[0], list(p[1]), list(p[2])]
print(q2)

# también con concatenación de listas
q3 = [p[0]] + [list(p[1])] + [list(p[2])]
print(q3)

# pero python tiene una herramienta para esto... el módulo copy (siguente video)



