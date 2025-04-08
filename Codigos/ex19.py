import math

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

delta = b ** 2 - 4*a*c

if delta > 0:
    print(f"Raiz 1: {(-b + math.sqrt(delta)/2*a)}")
    print(f"Raiz 2: {(-b - math.sqrt(delta)/2*a)}")
else:
    print("Não há raízes reais")