print("\033[1:32m PROGRAMA DE PROGRESSÃO ARITMÉTICA \033[m")
primertermo = float(input("Digita o 1º termo da progressão: "))
razao = float(input("Digita a razão da tua progressão: "))
cont = 0
while cont < 10:
    cont = cont + 1
    termos = primertermo + cont * razao
    print("O {}º termo é \033[1:32m {} \033[m".format(cont, termos))
print("\033[1:34m Obrigado por usares o meu programa!! \033[m")