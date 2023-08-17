print("Bem vindo à calculadora de média!! Aqui verás qual a tua média e se ela é boa ou não!")
nota1 = float(input("Digita a tua primeira nota: "))
nota2 = float(input("Digita a tua segunda nota: "))
media = (nota1 + nota2) / 2
if media < 5:
    print("Estás \033[31m REPROVADO \033[m")
elif media >= 5 and media < 6.9:
    print("Para a \033[33m RECUPERAÇÃO \033[m")
elif media > 6.9:
    print("Estás \033[32m APROVADO \033[m")
if media > 9.5:
    print("PARABÉNS!! Tiveste uma nota espetacular!")
