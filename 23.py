a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

if a <= b <= c:
    print("Valores em ordem crescente:", a, b, c)
elif a <= c <= b:
    print("Valores em ordem crescente:", a, c, b)
elif b <= a <= c:
    print("Valores em ordem crescente:", b, a, c)
elif b <= c <= a:
    print("Valores em ordem crescente:", b, c, a)
elif c <= a <= b:
    print("Valores em ordem crescente:", c, a, b)
else:
    print("Valores em ordem crescente:", c, b, a)