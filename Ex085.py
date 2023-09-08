valores = [[], []]
for c in range(1, 8):
    numero = int(input(f"Digita o {c}º número: "))
    if numero % 2 == 0:
        valores[0].append(numero)
    if numero % 2 != 0:
        valores[1].append(numero)

valores[0].sort()
valores[1].sort()
print(f"Os valores que digitaste foram: {valores}")
print(f"Os valores pares digitados foram: {valores[0]}")
print(f"Os valores impares digitados foram: {valores[1]}")
