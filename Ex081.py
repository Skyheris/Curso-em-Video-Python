print("---Analisador de Listas!---")
valores = []
num = int(input("Digita um número: "))
escolha = ""
while True:
    if num not in valores:
        valores.append(num)
        escolha = input("Desejas Continuar? [S/N]: ")
    else:
         print("Não digites valores repetidos!")

    if escolha.upper().strip()[0] == "S":
        num = int(input("Digita outro número: "))
    else:
        break


print(f"Da lista que digitaste: {valores}")
print(f"A lista tem {len(valores)} dígitos")
valores.sort(reverse=True)
print(f"A lista na forma decrescente fica: {valores}")
if 5 in valores:
    print(f"O valor 5 aparece {valores.count(5)} vezes")
else:
    print("Na tua lista não existe nenhum valor 5!")

