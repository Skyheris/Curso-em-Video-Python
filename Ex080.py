print("---Organizador de Números Automático!!---")
numeros = 0
lista = list()
for c in range(0, 5):
    numeros = int(input("Digita um número: "))
    if c == 0 or numeros > lista[-1]:
        lista.append(numeros)
    else:
        pos = 0
        while pos < len(lista):
            if numeros <= lista[pos]:
                lista.insert(pos, numeros)
                break
            pos += 1
print("-"*20)
print(f"A lista com os valores organizados é: {lista}")

