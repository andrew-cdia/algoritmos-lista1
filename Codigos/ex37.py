contador = 0

homens_castanho = 0
mulheres_160 = 0
mulheres = 0

while contador < 15:
    nome = input("Nome: ")
    altura = float(input("Altura: "))
    sexo = input("Sexo (M/F): ").lower
    corDosOlhos = input("Cor dos olhos (Azuis, Verdes, Castanhos): ").lower

    if sexo == "m" and corDosOlhos == "castanho":
        homens_castanho += 1
    if sexo == "f":
        mulheres += 1
        if altura < 1.6:
            mulheres_160 += 1

    contador += 1

print(f"Quantidade de mulheres: {mulheres}")
print(f"Quantidade de mulheres menores que 1.60m: {mulheres_160}")
print(f"Quantidade de homens de olhos castanhos: {homens_castanho}")