salario = float(input("Digite o salário atual: "))

if salario < 10000.00:
    reajuste = 0.55
elif salario <= 25000.00:
    reajuste = 0.20
else:
    reajuste = 0

novo_salario = salario * (1 + reajuste)

print("Reajuste salarial:", reajuste * 100, "%")
print("Novo salário:", novo_salario)
