# vamos a usar "deepcopy" el módulo copy:
# esta función se usa para copias de listas anidadas
# creando un nuevo objeto

from copy import deepcopy

f = p = [1, [2, 3], [4, 5]]
g = deepcopy(p)
print(g)

