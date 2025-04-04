qtd_hamburguer = int(input("Quantidade de Hamburgueres: "))
qtd_cheeseburguer = int(input("Quantidade de Cheeseburguers: "))
qtd_milkshake = int(input("Quantidade de Milkshakes: "))
qtd_cocas = int(input("Quantidade de Coca-Colas: "))

conta_final = (qtd_cheeseburguer * 4.1) + (qtd_hamburguer * 3.5) + (qtd_milkshake * 6) + (qtd_cocas * 2.5)

print(f"Conta final: {conta_final}")