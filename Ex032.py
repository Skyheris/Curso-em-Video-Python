ano = int(input("Diz-me um ano ao calhas: "))
bissexto = ano % 4
if bissexto == 0:
    print("O ano que escolheste é bissexto!")
else:
    print("O ano que escolheste não é bissexto!")
