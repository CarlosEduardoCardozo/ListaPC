def calcular_idades():
    idade_h1, idade_h2 = map(int, input("Digite as idades dos 2 homens separadas por espaço: ").split())
    idade_m1, idade_m2 = map(int, input("Digite as idades das 2 mulheres separadas por espaço: ").split())

    homem_mais_velho = max(idade_h1, idade_h2)
    mulher_mais_nova = min(idade_m1, idade_m2)

    soma_idades = homem_mais_velho + mulher_mais_nova
    produto_idades = min(idade_h1, idade_h2) * max(idade_m1, idade_m2)

    print("Soma das idades do homem mais velho com a mulher mais nova:", soma_idades)
    print("Produto das idades do homem mais novo com a mulher mais velha:", produto_idades)

calcular_idades()