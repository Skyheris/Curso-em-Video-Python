salario = float(input("Qual o teu salário? "))
aumento1 = salario * 1.10
aumento2 = salario * 1.15
if salario >= 1250:
    print("O teu salário passou a ser {:.1f}€".format(aumento1))
else:
    print("O teu salário passou a ser {:.1f}€".format(aumento2))
print("Parabéns pelo aumento!! Continua no bom caminho!!")
