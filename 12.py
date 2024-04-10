horas_professor1 = float(input("Digite a quantidade de horas aula do Professor 1: "))
valor_hora1 = float(input("Digite o valor por hora do Professor 1: "))

horas_professor2 = float(input("Digite a quantidade de horas aula do Professor 2: "))
valor_hora2 = float(input("Digite o valor por hora do Professor 2: "))

salario_total1 = horas_professor1 * valor_hora1
salario_total2 = horas_professor2 * valor_hora2

if salario_total1 > salario_total2:
    print("O Professor 1 tem o maior salário total.")
elif salario_total2 > salario_total1:
    print("O Professor 2 tem o maior salário total.")
else:
    print("Ambos os professores têm o mesmo salário total.")
