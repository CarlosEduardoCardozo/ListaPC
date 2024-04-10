valor_compra = float(input("Digite o valor do produto: "))

if valor_compra < 20.00:
    lucro = valor_compra * 0.45
else:
    lucro = valor_compra * 0.30

valor_venda = valor_compra + lucro

print(f"O valor da venda será de R${valor_venda:.2f}")
