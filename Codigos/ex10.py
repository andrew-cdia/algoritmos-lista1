nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2
print(f"Média: {media}")

if media >= 7:
    print("Aprovado por média")
else:
    print("Reprovado por média")