print("-="*14)
print("---Analisador de Pessoas!---")
print("-="*14)
dados_pessoais = {}
cont = 1
acumulador = media = 0
lista_dados = list()
mulheres = 0
while True:
    dados_pessoais['Nome'] = str(input(f"Nome da {cont}ª pessoa: "))
    dados_pessoais['Sexo'] = str(input(f"Sexo do(a) {dados_pessoais['Nome']}: ")).upper().strip()[0]
    dados_pessoais['Idade'] = int(input(f"Idade do(a) {dados_pessoais['Nome']}: "))
    lista_dados.append(dados_pessoais.copy())
    acumulador += dados_pessoais['Idade']
    cont += 1
    escolha = str(input("Queres Continuar? [S/N]: "))
    if escolha.strip()[0] not in "Ss":
        break
media = acumulador / (cont - 1)
print(f"Foram resgistadas {cont - 1} pessoas na lista!")
print("-="*10)
print(f"A média de idades do grupo é {media:.1f}")
print("-="*10)
print("Lista de Mulheres:")

for mulher in lista_dados:
    if mulher['Sexo'] == "F":
        print(f"{mulher['Nome']}")
        mulheres = 1

if mulheres == 0:
    print("Não existem mulheres na lista!")
print("-="*10)
print("Pessoas com idade acima da média:")
for pessoa in lista_dados:
    if pessoa['Idade'] > media:
        print(f"{pessoa['Nome']}")



