n = int(input("N: "))

h = 0
contador = 0

while contador <= n:
    h += 1/contador

    contador += 1

print(f"H: {h}")