import random
numeros = ()
for cont in range(0, 5):
    gerador = random.randint(0, 100)
    numeros += (gerador,)

numeros_organizados = tuple(sorted(numeros))
print(f"A lista gerada foi: {numeros}")
print(f"A lista dos números organizados é: {numeros_organizados}")
print(f"O maior número é o {numeros_organizados[4]} e o menor é {numeros_organizados[0]}")


