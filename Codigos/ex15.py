nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2

if media < 3:
    print("Reprovado sem rendimento")
elif media <= 6:
    print("Reprovado com insuficiência")
elif media <= 7:
    print("Aprovado com regular")
elif media <= 9:
    print("Aprovado com bom")
else:
    print("Aprovado com excelente")

