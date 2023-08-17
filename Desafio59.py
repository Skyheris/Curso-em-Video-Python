import time
print("Boas!! Apresento-te a minha semicalculadora!")
num1 = float(input("Digita o primeiro número: "))
num2 = float(input("Digita os segundo número: "))
soma = num1 + num2
multi = num1 * num2
subtrair = num1 - num2
subtrair2 = num2 - num1
dividir = num1 / num2
dividir2 = num2 / num1
escolha = int(input("""CALCULADORA!
Funções:
---SOMAR---[1]
---SUBTRAIR---[2]
---MULTIPLICAR---[3]
---DIVIDIR---[4]
---MOSTRAR O MAIOR---[5]
---DIGITAR NOVOS NÚMEROS---[6]
---SAIR---[7]
Digita o número da função escolhida:  """))
while escolha != 5:
    if escolha == 1:
        print("A soma é {}".format(soma))
    elif escolha == 2:
        print("A subtração entre {} e {} é {}, mas se for ao contrário é {}".format(num1, num2, subtrair, subtrair2))
    elif escolha == 3:
        print("A multiplicação entre os dois números é {}".format(multi))
    elif escolha == 4:
        print("O quociente entre {} e {} é {}, mas se for ao contrário é {}".format(num1, num2, dividir, dividir2))
    elif escolha == 5:
        if num1 < num2:
            print("O maior número é {}".format(num2))
        else:
            print("O maior número é {}".format(num1))
    elif escolha == 6:
        num1 = float(input("Digita o primeiro número: "))
        num2 = float(input("Digita os segundo número: "))
    time.sleep(2)
    escolha = int(input("""CALCULADORA!
        Funções:
        ---SOMAR---[1]
        ---SUBTRAIR---[2]
        ---MULTIPLICAR---[3]
        ---DIVIDIR---[4]
        ---MOSTRAR O MAIOR---[5]
        ---DIGITAR NOVOS NÚMEROS---[6]
        ---SAIR---[7]
        Queres fazer mais alguma operação?  """))
print("Obrigado por teres usado o meu programa!!")

