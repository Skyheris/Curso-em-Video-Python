import random

n1 = input("Digita um nome: ")
n2  = input("Digita outro nome: ")
n3 = input("Digita o último nome: ")
nomes = [n1, n2, n3]
escolhido = random.choice(nomes)
print(f"O nome escolhido foi {escolhido}")