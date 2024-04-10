nota1 = float(input("Digite a nota da 1ª avaliação: "))
nota2 = float(input("Digite a nota da 2ª avaliação: "))

media = (nota1 + nota2) / 2

if media >= 7.0:
    print("Aprovado")
else:
    nota_exame = float(input("Digite a nota do exame: "))
    media_final = (media + nota_exame) / 2
    if media_final >= 5.0:
        print("Aprovado")
    else:
        print("Reprovado")
