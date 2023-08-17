import random
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = int(input("Digita um número entre 0 e 10: "))
ne = random.choice(numeros)
cont = 0
while n != ne:
    cont = cont + 1
    ne = random.choice(numeros)
    n = int(input("Perdeste! Tenta outra vez ({}): ".format(ne)))
print("Ganhaste!! Parabéns! Tiveste de jogar {} vezes".format(cont))
