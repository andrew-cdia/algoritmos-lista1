idade = int(input("Idade: "))
sexo = input("Sexo (M/F): ").lower

if (sexo == "f" and idade > 60) or (sexo == "m" and idade > 65):
    print("Pode se aposentar")
else:
    print("Não pode se aposentar")