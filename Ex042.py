l1 = float(input("Digita o comprimento do primeiro lado: "))
l2 = float(input("Digita o comprimento do segundo lado: "))
l3 = float(input("Digita o comprimento do terceiro lado: "))

if (l1+l2) > l3 and (l1+l3) > l2 and (l2+l3) > l1:  # verificar se pode formar triângulo
    if l1 == l2 and l1 == l3:
        print("O triângulo é Equilátero!")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("O triângulo é Isósceles!")
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print("O triângulo é Escaleno!")
else:
    print("Não é possível formar um triângulo com os lados que forneceste!")

