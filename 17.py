numero = int(input("Digite um número de 1 a 12: "))

meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

if numero in meses:
    print(meses[numero])
else:
    print("Número inválido. Por favor, digite um número de 1 a 12.")
