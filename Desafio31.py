km = int(input("Quantos kilómetros vais percorrer? "))
p1 = km * 0.50
p2 = km * 0.45
if km <= 200:
    print("O preço do bilhete é {:.2f}€".format(p1))
else:
    print("O preço do bilhete é {:.2f}€".format(p2))