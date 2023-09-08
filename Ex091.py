from random import randint
from time import sleep
from operator import itemgetter
print("-="*10)
print("----JOGO DA SORTE----")
print("-="*10)
cont = 1
jog_num = {'Jogador1': randint(1, 6),
           'Jogador2': randint(1, 6),
           'Jogador3': randint(1, 6),
           'Jogador4': randint(1, 6)}
print("Valores Sorteados!")
for k, v in jog_num.items():
    print(f"{k} com {v} pontos")
    sleep(1)
ranking = sorted(jog_num.items(), key=itemgetter(1), reverse=True)
print("-="*7)
print("---RANKING---")
print("-="*7)
for k, v in ranking:
    print(f"{cont}º lugar: {k} com {v} pontos!")
    cont += 1
    sleep(1)
print("Obrigado por Jogares!!")





