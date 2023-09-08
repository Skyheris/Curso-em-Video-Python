import random
import time
print("-"*30)
print("    JOGA NA MEGA SENA!!    ")
print("-"*30)
numeros = random.randint(1, 60)
lista = list()
listacompleta = list()
num = 1
contagem = 1
cont = 1
jogos = int(input("Quantos jogos queres que sorteie? "))
while cont <= jogos:  # Necessário para receber os vários jogos!
    contagem = 0
    while True:  # Definição de casa jogo
        numeros = random.randint(1, 60)
        if numeros not in lista:  # Não ter números repetidos
            lista.append(numeros)
            contagem += 1
        if contagem >= 6:  # Limite de valores da lista
            break
    lista.sort()
    listacompleta.append(lista[:])  # Adicionar a lista a uma lista de jogos
    lista.clear() # Limpar para não se repetir
    cont += 1 # Passar para o próximo jogo

for list in listacompleta: # Imprimir a lista de forma bonita
    print(f"Jogo {num}: {list}")
    time.sleep(0.6)
    num += 1
print("BOA SORTE!!")


