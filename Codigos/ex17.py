idade = int(input("Idade: "))

if idade < 5 or idade < 60:
    print("Inválido")
elif idade >= 5 and idade <= 7:
    print("Infantil A")
elif idade >= 8 and idade < 10:
    print("Infantil B")
elif idade >= 11 and idade < 13:
    print("Juvenil A")
elif idade >= 14 and idade < 18:
    print("Juvenil B")
else:
    print("Sênior")