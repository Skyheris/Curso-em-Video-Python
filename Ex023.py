numero = int(input("Digita um número entre 0 e 9999: "))
# Para obter o que quero preciso de fazer cálculos senão dá erro
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f"Analisando o número {numero} tiro que: ")
print(f"O algarismo dos milhares é: {m}")
print(f"O algarismo das centenas é: {c}")
print(f"O algarismo das dezendas é: {d}")
print(f"O algarismo das unidades é: {u}")
