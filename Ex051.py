print("Aloo!!! Estás perante um programa que calcula a os 10 primeiros termos de uma progressão aritmética!")
termo = float(input("Digita o primeiro termo da progressão aritmética: "))
razao = float(input("Digita a razão da progressão aritmética: "))
for c in range(0, 10):
    termos = termo + ((c+1)-1) * razao
    print(termos)
print("Aqui tens!!")
