print("\033[1:34m Seja bem vindo(a) ao meu programa de Progressões Aritméticas!! \033[m")
termo1 = float(input("Digite o primeiro termo da progressão: "))
razao = float(input("Digite a razão da progressão: "))
numtermos = int(input("Digita a quantidade de termos que queres: "))
termos = 0
cont = 0
while cont < numtermos:
    cont = cont + 1
    termos = termo1 + cont *razao
    print("O {}º termo é \033[1:35m {} \033[m".format(cont, termos))
print("\033[1:32m FIM \033[m")
