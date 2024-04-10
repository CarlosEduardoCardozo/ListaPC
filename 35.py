def verificar_caracteristica(numero):
    if 1000 <= numero <= 9999:
        dezena_unidade = numero % 100
        milhar_centena = numero // 100
        terceiro_numero = dezena_unidade + milhar_centena
        if terceiro_numero**2 == numero:
            return True
    return False

numero = int(input("Digite um número de 4 dígitos: "))
if verificar_caracteristica(numero):
    print("O número obedece à característica.")
else:
    print("O número não obedece à característica.")