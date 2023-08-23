print("---$BANCO OLIVEIRA$---")
cont = 0
valorlevantado = int(input("Quanto deseja levantar? "))
resto = valorlevantado
cont50 = 0
cont20 = 0
cont10 = 0
cont1 = 0
while resto != 0:

    if resto >= 50:
        cont50 = (resto // 50)
        resto = resto % 50

    elif resto >= 20:
        cont20 = (resto // 20)
        resto = resto % 20

    elif resto >= 10:
        cont10 = (resto // 10)
        resto = resto % 10

    else:
        cont1 = resto // 1
        resto = 0

print("-=-"*10)
print(f"Foram debitadas {cont50} notas de 50€")
print(f"Foram debitadas {cont20} notas de 20€")
print(f"Foram debitadas {cont10} notas de 10€")
print(f"Foram debitadas {cont1} moedas de 1€")
print("-=-"*10)
print("Obrigado por ter vindo ao Banco OLIVEIRA!")


