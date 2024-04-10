sigla_estado = input("Digite a sigla do estado: ").upper()

if sigla_estado == "RJ":
    print("Carioca")
elif sigla_estado == "SP":
    print("Paulista")
elif sigla_estado == "MG":
    print("Mineiro")
else:
    print("Outros")
