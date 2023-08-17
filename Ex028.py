import random 
numeros = [0, 1, 2, 3, 4, 5]
n = random.choice(numeros)
ne = int(input("Digita um número entre 0 e 5: "))
if n == ne:
    print("Tu ganhaste, PARABÉNS!!")
else:
    print("Tenta novamente :(")
print("Obrigado por teres tentado :)")
