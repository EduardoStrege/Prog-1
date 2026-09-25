preço = float(input("Digite o preço do produto: \n"))
quant = int(input("Digite a quantidade de itens \n"))
valor_total = preço * quant
print(f"O valor total da compra é : R${valor_total:.2f}")