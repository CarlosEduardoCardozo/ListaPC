def operacoes_com_resto():
    a, b = map(int, input("Digite dois números inteiros separados por espaço: ").split())
    resto_divisao = a % b

    if resto_divisao == 1:
        print("Soma dos números mais o resto da divisão:", a + b)
    elif resto_divisao == 2:
        if a % 2 == 0:
            print("O primeiro número é par")
        else:
            print("O primeiro número é ímpar")
        if b % 2 == 0:
            print("O segundo número é par")
        else:
            print("O segundo número é ímpar")
    elif resto_divisao == 3:
        print("Multiplicação da soma dos números pelo primeiro:", (a + b) * a)
    elif resto_divisao == 4:
        if b != 0:
            print("Divisão da soma dos números pelo segundo:", (a + b) / b)
        else:
            print("Divisão por zero não é permitida")
    else:
        print("Quadrado dos números:", a**2, b**2)


operacoes_com_resto()
