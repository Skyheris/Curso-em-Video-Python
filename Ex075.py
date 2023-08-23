print("---Análise de Números!---")
numero = 0
tupla_numeros = ()
tupla_pares = ()
for cont in range (0, 4):
    numero = int(input("Digita um valor entre 0 e 10: "))
    while numero > 10 and numero:
        print("Erro! Tenta outra vez!")
        numero = int(input("Digita um valor entre 0 e 10: "))
    tupla_numeros += (numero,)
    if numero % 2 == 0:
        tupla_pares += (numero,)

if tupla_numeros.count(9) == 0:
    print(f"O valor 9 não apareceu nenhuma vez!")

elif tupla_numeros.count(9) == 1:
    print(f"O valor 9 apareceu 1 vez!")

elif tupla_numeros.count(9) > 1:
    print(f"O valor 9 apareceu {tupla_numeros.count(9)} vezes!")
if 3 in tupla_numeros:
    print(f"O 1º nº3 foi registado na posição {tupla_numeros.index(3)}")
else:
    print("Não foram digitados 3!")
if len(tupla_pares) > 0:
    print(f"Os números pares registados foram: {tupla_pares} ")
else:
    print("Não foram digitados números pares!")
print("Obrigado por teres utilizado o meu programa!")




