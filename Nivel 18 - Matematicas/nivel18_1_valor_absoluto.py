"""
Función que encuentre el valor absoluto de un nº (igual que abs())
Hay que tener cuidado, ya que la que elaboremos, va a pisar a la
predefinida
"""
x = -20
print(abs(20))  # --> 20

def valor_absoluto(num):
    if num >= 0 :
        return num
    else:
        return -num

print(valor_absoluto(-20))  # --> 20
