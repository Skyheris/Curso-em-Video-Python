n1 = int(input("Digita o primeiro número inteiro: "))
n2 = int(input("Digita o segundo número inteiro: "))
n3 = int(input("Digita o terceiro número inteiro: "))
#Verificar quem são os menores e maiores
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
print("O maior valor é {} e o menor valor é {}".format(maior, menor))