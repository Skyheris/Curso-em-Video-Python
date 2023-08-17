print("Olá!! Espero que estejas bem! Este programa vai ler os 2 números que digitares e vai compará-los!")
num1 = float(input("Digita o primeiro número: "))
num2 = float(input("Digita o segundo número: "))
if num1 > num2:
    print("O maior número é {}".format(num1))
elif num1 < num2:
    print("O maior número é {}".format(num2))
else:
    print("Os dois números são iguais!")
