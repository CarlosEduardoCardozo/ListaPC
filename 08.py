ano_nascimento = int(input("Digite o ano de nascimento: "))

if ano_nascimento > 0 and ano_nascimento <= 2024:
    idade = 2024 - ano_nascimento
    print(f"A idade da pessoa é {idade} anos.")
else:
    print("Ano de nascimento inválido.")
