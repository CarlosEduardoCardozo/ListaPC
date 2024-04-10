nota1 = float(input("Digite a nota da 1ª avaliação: "))
nota2 = float(input("Digite a nota da 2ª avaliação: "))

media = (nota1 + nota2) / 2

if media >= 6:
    print(f"O aluno foi aprovado com média {media:.2f}.")
else:
    print(f"O aluno foi reprovado com média {media:.2f}.")
