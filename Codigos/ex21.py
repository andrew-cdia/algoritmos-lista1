a = float(input("Angulo A: "))
b = float(input("Angulo B: "))
c = float(input("Angulo C: "))

if a > 90 and b > 90 and c > 90:
    print("Acutângulo")
elif a == 90 or b == 90 or c == 90:
    print("Retângulo")
else:
    print("Obtusângulo")