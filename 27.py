a = float(input("Digite o comprimento do lado a: "))
b = float(input("Digite o comprimento do lado b: "))
c = float(input("Digite o comprimento do lado c: "))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print("Os valores formam um triângulo equilátero.")
    elif a == b or a == c or b == c:
        print("Os valores formam um triângulo isósceles.")
    else:
        print("Os valores formam um triângulo escaleno.")
else:
    print("Os valores lidos não formam um triângulo.")