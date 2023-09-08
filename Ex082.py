print("---Par e Impares!---")
print("-=-"*10)
listatotal = []
listapar = []
listaimpar = []
num = int(input("Digita um número: "))
escolha = ""
while True:
    if num not in listatotal:
        listatotal.append(num)
    else:
        print("Não digites valores repetidos!")

    if num % 2 == 0 or num == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
    escolha = input("Queres continuar? [S/N]: ")
    if escolha.upper().strip()[0] == "S":
        num = int(input("Digita outro número: "))
    else:
        break

listatotal.sort()
listapar.sort()
listaimpar.sort()
print(f"A lista organizada dos números que registaste é: {listatotal}")
print(f"A lista organizada dos números pares que regitaste é: {listapar}")
print(f"A lista organizada dos números impares que registaste é: {listaimpar}")
print("-"*20)
print("Obrigado por teres utilizado o meu programa!!!")
