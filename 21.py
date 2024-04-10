a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

if a >= b and a >= c:
    print("O maior valor é:", a)
elif b >= a and b >= c:
    print("O maior valor é:", b)
else:
    print("O maior valor é:", c)