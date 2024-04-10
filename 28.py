def ordenar_valores():
    opcao = int(input("Digite a opção (1 para crescente, 2 para decrescente, 3 para maior no meio): "))
    a, b, c = map(float, input("Digite os valores de a, b, c separados por espaço: ").split())

    if opcao == 1:
        if a <= b <= c:
            print("Ordem crescente:", a, b, c)
        elif a <= c <= b:
            print("Ordem crescente:", a, c, b)
        elif b <= a <= c:
            print("Ordem crescente:", b, a, c)
        elif b <= c <= a:
            print("Ordem crescente:", b, c, a)
        elif c <= a <= b:
            print("Ordem crescente:", c, a, b)
        else:
            print("Ordem crescente:", c, b, a)
    elif opcao == 2:
        if a >= b >= c:
            print("Ordem decrescente:", a, b, c)
        elif a >= c >= b:
            print("Ordem decrescente:", a, c, b)
        elif b >= a >= c:
            print("Ordem decrescente:", b, a, c)
        elif b >= c >= a:
            print("Ordem decrescente:", b, c, a)
        elif c >= a >= b:
            print("Ordem decrescente:", c, a, b)
        else:
            print("Ordem decrescente:", c, b, a)
    elif opcao == 3:
        if a >= b >= c:
            print("Maior valor entre a, b, c:", b, a, c)
        elif a >= c >= b:
            print("Maior valor entre a, b, c:", c, a, b)
        elif b >= a >= c:
            print("Maior valor entre a, b, c:", a, b, c)
        elif b >= c >= a:
            print("Maior valor entre a, b, c:", c, b, a)
        elif c >= a >= b:
            print("Maior valor entre a, b, c:", a, c, b)
        else:
            print("Maior valor entre a, b, c:", b, c, a)

ordenar_valores()
