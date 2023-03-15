'''
la elección va a depender de varios factores, ppalmente de las lineas de código.
El modo iterativo suele ser mas sencillo.
A nivel de eficiencia, suelen ser similares con las misma complejodad --> O(n)
Las recursivas suelen llevar algo más de tiempo, y guardan en momoria todas las operaciones y 
tiene la limitación de 1000 llamadas. Si se excede, se genera una excepción.

esto lo podemos ver:
import sys
sys.getrecursionlimit() --> da un resultado de 1000 

para cambiarlo:
sys.setrecursionlimit(2000) --> lo cambia a 2000

'''