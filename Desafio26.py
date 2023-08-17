frase = str(input("Digita uma frase: ")).strip()
contagem = frase.upper().count('A')
apareceu1 = frase.upper().find("A")
apareceu2 = frase.upper().rfind("A")
print(f"Na frase aparecem {contagem} vezes a letra A")
print(f"A primeira vez que aparece é na posição {apareceu1}")
print(f"A última vez que aparece é na posição {apareceu2}")

