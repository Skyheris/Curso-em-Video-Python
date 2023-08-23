print("Olá!! Espero que gostes do meu gerador de listas!")
lista = []
escolha = ""
while True:
    numeros = float(input("Digita o número que quiseres: "))

    if numeros not in lista: # Verificar se o número está na lista!
        lista.append(numeros)
    else:
        print("Não repitas os números!")
        print("-" * 15)

    escolha = input("Desejas Continuar? [S/N] ")

    if escolha.upper().strip() == "N": # Rutura do loop
        break
print(f"A lista que digitaste é {lista}")
lista.sort()
print(f"Se eu organizar a tua lista, por ordem crescente, ela fica assim : {lista}")
