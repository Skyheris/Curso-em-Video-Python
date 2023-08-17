print("\033[1:34m Bem vindo(a)! Este é o meu calculador de fatoriais! \033[m")
num = int(input("Digita um número inteiro: "))
cont = 1
resultado = 1
while cont < num:
    resultado = resultado * cont
    cont = cont + 1
print("O fatorial de {} é {}".format(num, resultado))