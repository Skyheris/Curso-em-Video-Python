def area(c, l):
    tamanho = c * l
    print(f"A área do terreno de {c}x{l} é igual a {tamanho}m2")


def linha():
    print("-="*10)


linha()
print("AREADOR DE TERRENOS")
linha()

c = float(input("Comprimento (m): "))
l = float(input("Largura (m): "))

area(c, l)
