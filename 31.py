def controle_temperatura():
    temperatura = int(input("Digite a temperatura de trabalho do alumínio (em °C): "))

    if temperatura <= 500:
        print("Temperatura Inválida")
    elif temperatura < 700:
        print("Aquecimento Ligado em 100%")
    elif temperatura < 735:
        print("Aquecimento Ligado em 50%")
    elif temperatura >= 735 and temperatura <= 779:
        print("Aquecimento Desligado")
    elif temperatura > 780 and temperatura < 1000:
        print("Superaquecimento")
    else:
        print("Temperatura inválida")

controle_temperatura()
