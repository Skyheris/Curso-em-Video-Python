from random import randint
from time import sleep
numeros = list()


def sorteia():
    print("Sorteando 5 números: ",end="")
    for cont in range(0, 5):
        num = randint(1, 10)
        print(f"{num}",end= " ")
        sleep(0.4)
        numeros.append(num)
    print("SORTEADO!")
    print(f"Os números sorteados foram: {numeros}")


def somapar():
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f"A soma dos números pares da lista é: {soma}")


sorteia()
sleep(0.5)
somapar()











