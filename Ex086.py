c1 = 0
c2 = 0
matriz1 = []
matriz2 = []
matriz3 = []
for c in range (0, 3):
        numero = int(input(f"Digita o número [{c1},{c2}]: "))
        c2 += 1
        matriz1.append(numero)
c2 = 0
for c in range(0, 3):
        c1 = 1
        numero = int(input(f"Digita o número [{c1},{c2}]: "))
        c2 += 1
        matriz2.append(numero)
c2 = 0
for c in range(0, 3):
    c1 = 2
    numero = int(input(f"Digita o número [{c1},{c2}]: "))
    c2 += 1
    matriz3.append(numero)
print("-----MATRIZ-----")
print(f"[ {matriz1[0]} ] [ {matriz1[1]} ] [ {matriz1[2]} ]")
print(f"[ {matriz2[0]} ] [ {matriz2[1]} ] [ {matriz2[2]} ]")
print(f"[ {matriz3[0]} ] [ {matriz3[1]} ] [ {matriz3[2]} ]")


