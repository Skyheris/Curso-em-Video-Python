print("Olá!! Este programa vai calcular a soma dos números pares que digitares!!")
soma = 0
contador = 0
for c in range(0, 6):
    num = int(input("Digita um número: "))
    if num % 2 == 0:
        soma = soma + num
        contador = contador + 1
print("A soma de {} números é igual a {}".format(contador, soma))
