preço = input("Digite o preço do produto: \n")
quant = input("Digite a quantidade de produtos: \n")
desc = input("Digite uma porcentagem de desconto: \n")
preço = float(preço)
quant = int(quant)
desc = float(desc)

valor_compra = (preço * quant)
valor_desconto = (valor_compra * desc / 100)
valor_final = valor_compra - valor_desconto

print(f"Preço : R$ {preço}")
print(f"Desconto : {desc}%")
print(f"Valor final {valor_final}")