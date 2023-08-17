import random

n1 = input("Digita um nome: ")
n2 = input("Digita outro nome: ")
n3 = input("Digita outro nome: ")
n4 = input("Digita o último nome: ")
nomes = [n1, n2, n3, n4]
ordem = random.sample(nomes , k=4)
print(f"A ordem escolhida foi: {ordem}")
