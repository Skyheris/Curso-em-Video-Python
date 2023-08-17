import math

ca = float(input("Digita o comprimento do cateto adjacente: "))
co = float(input("Digita o comprimento do cateto oposto: "))
h = math.sqrt((ca**2)*(co**2))
print(f"De acordo com os valores que digitaste, o valor da hipotenusa é: {h}")
