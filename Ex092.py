print("-="*15)
print(" ---Analizador de Pessoas---")
print("-="*15)
informacao = dict()
informacao['Nome'] = str(input("Nome: "))
ano_nascimento = int(input("Ano de Nascimento: "))
idade = 2023 - ano_nascimento
informacao['Idade'] = idade
informacao['CTPS'] = int(input("Carteira de Trabalho(0 não trabalha): "))

if informacao['CTPS'] > 0:
    informacao['Contratação'] = int(input("Ano de Contratação: "))
    informacao['Salário'] = float(input("Salário: "))
    print("-="*20)
else:
    print("-="*15)
    for key, value in informacao.items():
        print(f"{key} tem o valor de {value}")

if informacao['CTPS'] > 0:
    aposentadoria = (informacao['Contratação'] - ano_nascimento) + 35
    informacao['Aposentadoria'] = aposentadoria
    for key, value in informacao.items():
        print(f"{key} tem o valor de {value}")
print("-"*30)
print(f"Os dados do(a) {informacao['Nome']} foram guardados com sucesso!")

