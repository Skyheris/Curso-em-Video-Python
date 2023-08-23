import random
print("\033[1:34m Bem Vindo(a) ao jogo do Par ou Ímpar!! Boa Sorte \033[m")
print("-"*35)
computador = int(random.randint(0, 100))
numerojogador = int(input("Digita um número: "))
escolhajogador = str(input("Par ou Impar parceiro? "))
cont = 0
while True:
    print("-=-" * 15)
    if escolhajogador.upper().strip() == "PAR" and (computador + numerojogador) % 2 == 0:
        cont += 1
    elif escolhajogador.upper().strip() == "IMPAR" and (computador + numerojogador) % 2 != 0:
        cont += 1
    else:
        print("\033[31mPerdeste\033[m! Tenta outra vez!")
        break

    numerojogador = int(input("\033[32mGanhaste\033[m, pois saiu {}!! Digita outro número: ".format(computador + numerojogador)))
    escolhajogador = str(input("Par ou Impar Parceiro? ")).upper().strip()
if cont > 0:
    print(f"Obrigado por jogares! Tu ganhaste {cont} vezes!")
else:
    print("Mesmo não tendo ganho, volta a tentar! Não desistas!")
