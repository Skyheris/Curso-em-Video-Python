print("\033[1:34m Boas!! Queres saber se ainda vais a tempo de te alistar no serviço militar?? Então este programa é para ti! \033[m")
nome = str(input("Qual é o teu nome? "))
ano = int(input("Qual o ano em que nasceste {}? ".format(nome)))
idade = 2023 - ano
espera = 18 - idade
if idade < 18:
    print("Ainda não tens idade para te alistar no exército, espera {} anos!")
elif idade >= 18 and idade <= 45:
    print("Está na altura de te alistares!! BORAA")
elif idade > 45:
    print("Já é tarde! Agora é sopas e descanso :)")
print("Obrigado por teres usado o meu programa!!")
