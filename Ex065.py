print("«»"*20)
print("\033[1:34m        →SOMADOR DE NÚMEROS← \033[m")
print("«»"*20)
acumulador = maior = menor = cont = 0  # Definição das variáveis
escolha = ""
while escolha.upper() != "N":  # Início do loop
    numero = int(input("Digite um número inteiro: "))
    cont = cont + 1
    acumulador = acumulador + numero
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    escolha = str(input("Queres continuar? [S/N] ")).upper().strip()[0]  # Fim do Loop
media = acumulador / cont
print("Tu digitaste {} número e a média entre eles foi {}".format(cont, media))  # ↓Respostas↓
print("O maior número foi {} e o menor foi {}".format(maior, menor))

