cont = 0
acumulador = 0
maior = 0
menor = 0
idadevelha = 0
homemvelho = ""
for c in range(1, 5):
    nome = input("Digita o nome da {} pessoa: ".format(c))
    sexo = input("Digita o sexo da {} pessoa (Homem ou Mulher): ".format(c))
    idade = int(input("Digita a idade da {} pessoa: ".format(c)))
    acumulador = acumulador + idade
    media = acumulador / 4
    if sexo.upper() == "MULHER" and idade:
        cont = cont + 1
    if c == 1:
        maior = idade
        menor = idade
    else:
        if idade > maior:
            maior = idade
        if idade < menor:
            menor = idade
    if sexo.upper() == "HOMEM" and idade > idadevelha:
        homemvelho = nome
        idadevelha = idade
print("A média das idades é {} anos, o homem mais velho é o {} e existem {} mulheres com menos de 20 anos".format(media, homemvelho, cont))


