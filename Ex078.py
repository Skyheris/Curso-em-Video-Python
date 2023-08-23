print("---Bem vindo(a) ao leitor de números!!---")
lista = []
numeros = 0
max_positions = []
min_positions = []

for n in range(0, 5):
    numeros = int(input(f"Digita o número na posição {n}: "))
    lista += (numeros,)
print(f"A lista registada tem os seguintes valores: {lista} ")

max = max(lista)
min = min(lista)

for imax, valor in enumerate(lista):
    if valor == max:
        max_positions += (imax,)

for imin, valor in enumerate(lista):
    if valor == min:
        min_positions += (imin,)

if len(max_positions) > 1:
    print(f"O maior valor da lista foi o {max} nas posições {max_positions}")
else:
    print(f"O maior valor da lista foi o {max} na posição {lista.index(max)}")

if len(min_positions) > 1:
    print(f"O menor valor da lista foi o {min} nas posições {min_positions}")
else:
    print(f"O menor valor da lista foi o {min} na posição {lista.index(min)}")




