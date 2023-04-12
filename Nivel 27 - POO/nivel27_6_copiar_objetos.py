'''
En python hay que tener cuidado cuando se copian objetos, 
ya que lo que frecuentemente pensamos que copiamos, pero lo 
que hacemos es referenciar el mismo objeto.

por ejemplo, para copiar una lista, lo podemos hacer de 3 maneras:

a = [1, 2, 3]

* b = a[:] 
* c = list(a)
* con las funciones copy y deepcopy del módulo Copy (hay que importar el módulo)
'''