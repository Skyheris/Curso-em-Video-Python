import time
print("«", "-"*10, end="")
print("\033[32mTABUADAS\033[m", end="")
print("-"*10, "»")
numeros = int(input("Digita o número que desejas: "))
cont = 0
escolha = ""
while 0 + numeros > 0:
    print(f"Tabuada do {numeros}")
    for c in range (1, 11):
        print(f"{numeros} x {c} = \033[34m{numeros * c} \033[m ")
        time.sleep(0.3)
    escolha = int(input("""Queres continuar?
    SIM [ 1 ]
    NÃO [ -2 ]
    Escolha: """))
    if escolha > 0:
        numeros = int(input("Digita outro número que desejes: "))
    else:
        break
print("Obrigado por utilizares o meu programa")


