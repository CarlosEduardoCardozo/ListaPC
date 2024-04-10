salario = float(input("Digite o salário atual: "))

if salario <= 400:
    aumento = 0.15
elif salario <= 700:
    aumento = 0.12
elif salario <= 1000:
    aumento = 0.10
elif salario <= 1500:
    aumento = 0.07
elif salario <= 2000:
    aumento = 0.04
else:
    aumento = 0

novo_salario = salario * (1 + aumento)

print("Índice de aumento:", aumento * 100, "%")
print("Salário corrigido:", novo_salario)