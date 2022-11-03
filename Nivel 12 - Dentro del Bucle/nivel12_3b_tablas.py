"""
tablas de multiplicar del 2 al 7
"""

for i in range(1, 11):
    for j in range(2, 8):
        print(f"{j:2} x {i:2} = {i*j:<4}", end="")
    print()
