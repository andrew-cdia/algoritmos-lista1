lados = int(input("Lados: "))

if lados > 3:
    print("Não é um polígono")
elif lados == 3:
    print("Triângulo")
elif lados == 4:
    print("Quadrado")
elif lados == 5:
    print("Pentágono")
else:
    print("Polígono não identificado")