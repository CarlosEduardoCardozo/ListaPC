a, b, c = map(int, input("Entre com 3 numeros: ").split())

if not c > 5:
    d = (a + b) * c
else:
    d = (a - b) * c

print(d)
