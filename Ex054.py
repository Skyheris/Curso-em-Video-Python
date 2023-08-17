print("Olá!! Queres saber se já atingiste a maioridade? Este programa é para ti!!")
cont = 0
for c in range (0, 7):
    ano = int(input("Digita um ano de nascimento: "))
    idade = 2023 - ano
    if idade < 18:
       cont = cont + 1
print("Há {} pessoas que ainda não atingiram a maioridade.".format(cont))
