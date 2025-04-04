salario = float(input("Salario: "))

if salario < 800:
    salarioReajustado = salario * 1.15
elif salario < 1500:
    salarioReajustado = salario * 1.1
else:
    salarioReajustado = salario * 1.05

print(f"Salário Reajustado: {salarioReajustado}")