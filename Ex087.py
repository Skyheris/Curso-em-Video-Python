matriz1 = []
matriz2 = []
matriz3 = []
somapar = mai = somacoluna = 0
c1 = 0
c2 = 0
for c in range(0,3):
    numero = int(input(f"Digita o número [{c1},{c2}]: "))
    c2 += 1
    matriz1.append(numero)
    if numero % 2 == 0:
        somapar += numero
c2 = 0
for c in range(0, 3):
    c1 = 1
    numero = int(input(f"Digita o número [{c1},{c2}]: "))
    c2 += 1
    matriz2.append(numero)
    if numero % 2 == 0:
        somapar += numero
    for n in matriz2:
        if n > mai:
            mai = n
c2 = 0
for c in range(0, 3):
    c1 = 2
    numero = int(input(f"Digita o número [{c1},{c2}]: "))
    c2 += 1
    matriz3.append(numero)
    if numero % 2 == 0:
        somapar += numero
somacoluna = matriz1[2] + matriz2[2] + matriz3[2]
print("A Matriz registada foi:")
print(f"[ {matriz1[0]} ] [ {matriz1[1]} ] [ {matriz1[2]} ]")
print(f"[ {matriz2[0]} ] [ {matriz2[1]} ] [ {matriz2[2]} ]")
print(f"[ {matriz3[0]} ] [ {matriz3[1]} ] [ {matriz3[2]} ]")
print("-"*15)
print(f"A soma de todos os valores pares registados é: {somapar}")
print(f"A soma dos valores da 3º coluna é: {somacoluna}")
print(f"O maior valor da 2º linha é: {mai}")
