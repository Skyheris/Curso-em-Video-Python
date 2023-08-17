print("Bem vindo ao programa que te vai dizer se podes ou não, comprar uma casa!")
nome = input("Qual é o seu nome? ")
casa = float(input("Qual o preço da casa? "))
salario = float(input("Qual o teu salário? "))
tempo = int(input("Em quantos anos vais pagar a casa? "))
prest = casa / (tempo*12)
sal30 = salario * 0.3

if prest < sal30:
    print("Parabéns {}!! Vais poder adquirir a tua tão sonhada casa!".format(nome))
elif prest >= sal30:
    print("Desculpa {}, mas ou vais ter de arranjar uma casa mais barata ou tens de ganhar mais dinheiro, força!!".format(nome))


