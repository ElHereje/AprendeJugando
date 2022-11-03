"""
n! = 1 * 2 * 3 * ... * n
n! = n * n-1 * n-1 * n-3 * ... * 1

También se encuentra en el modulo math
"""
import math

x = 10
print(math.factorial(10))

# forma 1
def mi_factorial(num):
    f = 1
    for i in range(1,num+1):
        f *= i
    return f

# forma 2
def mi_factorial2(num):
    f = 1
    for i in range(num):
        f *= num-i
    return f


print(mi_factorial(10))
print(mi_factorial2(10))

