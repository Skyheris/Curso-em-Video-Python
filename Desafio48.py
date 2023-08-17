s = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        cont = cont + 1
        s = s + c
print("A soma de {} valores é {}".format(cont, s))
