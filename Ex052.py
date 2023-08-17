print("Bem vindo(a) ao mostrador de números primos!!")
num = int(input("Digita um número natural: "))
contador = 0
for c in range(1, num + 1):
    if num % c == 0:
        contador = contador + 1
if contador == 2:
    print("O número {} é PRIMO!!".format(num))
else:
    print("O número {} não é primo pois ele é divisível {} vezes!".format(num ,contador))
