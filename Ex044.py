print("Bem vindo(a)! Este programa vai calcular o preço de um produto de acordo com o método de pagamento!")
preco = float(input("Digita o preço do produto: "))
metodo = str(input("""Métodos de pagamento:
À vista (dinheiro/cheque) [ vista ]
À vista no cartão [ vistacard ]
2x no cartão [ cardtwo ]
3x no cartão [ cardthree ]
Como queres pagar?? """))
vista = preco * 0.9
vistacard = preco * 0.95
cardtwo = preco
cardthree = preco * 1.20
if metodo == "vista":
    print("O preço fica em {}€".format(vista))
elif metodo == "vistacard":
    print("O preço fica em {}€".format(vistacard))
elif metodo == "cardtwo":
    print("O preço fica em {}€".format(cardtwo))
elif metodo == "cardthree":
    print("O preço fica em {}€".format(cardthree))
else:
    print("Erro, tenta outra vez")
