a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
operacao = int(input("Digite o código da operação (1 – Adição, 2 – Subtração, 3 – Multiplicação, 4 – Divisão): "))

if operacao == 1:
    resultado = a + b
elif operacao == 2:
    resultado = a - b
elif operacao == 3:
    resultado = a * b
elif operacao == 4:
    resultado = a / b
else:
    resultado = None
    print("Código de operação inválido.")

if resultado is not None:
    print("Resultado da operação:", resultado)