print("-"*7, end= "")
print("Somatório de número!!", end="")
print("-"*7)
cont = 0
acumulador = 0
numero = int(input("Digita um número inteiro: "))
while numero != 999:
    cont += 1
    numero = int(input("Digita um número inteiro: "))
    if numero == 999:
        break
    acumulador += numero
print(f"Tu escreveste {cont} números e a soma deles é {acumulador}")