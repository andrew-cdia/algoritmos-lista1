contador = 0

while contador < 10:
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F):").lower

    if sexo == "m" and idade >= 21:
        print(nome)
    
    contador += 1

