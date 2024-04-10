def calculadora():
    valor_opcao = int(input("Digite um valor de 0 a 4: "))
    if valor_opcao == 0:
        a, b = map(float, input("Digite dois números separados por espaço: ").split())
        print("Soma:", a + b)
    elif valor_opcao == 1:
        a, b = map(float, input("Digite dois números separados por espaço: ").split())
        print("Subtração:", a - b)
    elif valor_opcao == 2:
        a, b = map(float, input("Digite dois números separados por espaço: ").split())
        print("Multiplicação:", a * b)
    elif valor_opcao == 3:
        a, b = map(float, input("Digite dois números separados por espaço: ").split())
        if b != 0:
            print("Divisão:", a / b)
        else:
            print("Divisão por zero não é permitida")
    elif valor_opcao == 4:
        a, b = map(float, input("Digite dois números separados por espaço: ").split())
        print("Média:", (a + b) / 2)
    else:
        print("Valor errado. Programa encerrado sem cálculos")

calculadora()
