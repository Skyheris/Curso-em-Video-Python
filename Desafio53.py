print("Bem vindo(a) ao detetor de palíndromos!!!")
frase = str(input("Digita a palavra/frase que quiseres: "))
fraseinv = frase[::-1]
frasefin = frase.upper().replace(" ", "")
fraseinvfin = fraseinv.upper().replace(" ", "")
if frasefin == fraseinvfin:
    print("A palavra/frase que digitaste é um palíndromo!")
else:
    print("A palavra/frase que digitaste não é um palíndromo!")