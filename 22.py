a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

if a >= b and a >= c:
    if b >= c:
        soma_maiores = a + b
    else:
        soma_maiores = a + c
elif b >= a and b >= c:
    if a >= c:
        soma_maiores = b + a
    else:
        soma_maiores = b + c
else:
    if a >= b:
        soma_maiores = c + a
    else:
        soma_maiores = c + b

print("A soma dos 2 maiores valores é:", soma_maiores)