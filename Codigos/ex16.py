altura = float(input("Altura: "))
sexo = input("Sexo (M/F): ").lower

if sexo == "f":
    peso_ideal = (61.2 * altura) - 44.7
else:
    peso_ideal = (72.7 * altura) - 58

print(f"Peso ideal: {peso_ideal} kg")