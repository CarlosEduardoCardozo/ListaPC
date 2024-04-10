nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

conceito = ''
if media >= 9.0:
    conceito = 'A'
elif media >= 7.5:
    conceito = 'B'
elif media >= 6.0:
    conceito = 'C'
elif media >= 4.0:
    conceito = 'D'
else:
    conceito = 'E'

situacao = "APROVADO" if conceito in ['A', 'B', 'C'] else "REPROVADO"

print("Notas:", nota1, "e", nota2)
print("Média:", media)
print("Conceito:", conceito)
print("Situação:", situacao)