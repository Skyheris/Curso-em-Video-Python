print(">"*5, "!ANALISADOR DE PRODUTOS!", "<"*5)
produto = str(input("Qual o Produto que deseja registar? ")).strip()
preco = int(input("Qual o preço do Produto? "))
print("-=-"*10)
acumulador = 0
produto_barato = ""
preco_barato = 0
cont1000 = 0
escolha = ""
menor = 0
cont = 0
while preco != 0:
    acumulador += preco
    escolha = str(input("Deseja Continuar?[S/N] "))
    cont += 1
    print("-=-"*10)
    if preco > 1000:
        cont1000 += 1
    if cont == 1 or preco < preco_barato:
        produto_barato = produto
        preco_barato = preco
    if escolha.upper().strip() == "S":
        produto = str(input("Qual o Produto que deseja registar? ")).lstrip()
        preco = int(input("Qual o preço do Produto? "))
        print("-=-"*10)
    else:
        break
print(f"No total você gastou {acumulador}€")
print(f"Você comprou {cont1000} que custam mais de 1000€")
print(f"O produto mais barato que compraste foi {produto_barato}")












