print("Bem vindo(a)!! Este programa vai mostrar a tabuada de um número, mas agora usando a função for!")
num = int(input("Digita um número: "))
fim = num * 10
for c in range(num, fim+1, num):
    print(c)