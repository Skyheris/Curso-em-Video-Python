temp = []
principal = []
mai = men = 0
while True:
    temp.append(str(input("Digita o nome da pessoa: ")))
    temp.append(int(input("Digita o peso da pessoa: ")))
    if len(principal) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    principal.append(temp[:])
    temp.clear()
    escolha = str(input("Deseja continuar? [S/N]: "))
    print("-"*25)
    if escolha.strip()[0] in "Nn":
        break

print("-=-"*10)
print(f"O número de pessoas cadastradas foi {len(principal)}")
print(f"A(s) pessoa(s) mais pesada(s) tem(têm) {mai}kg. Ela(s) é(são): ",end="")
for p in principal:
    if p[1] == mai:
        print(f"{p[0]}, ", end="")
print()
print(f"A(s) pessoa(s) mais leve(s) tem(têm) {men}kg. Ela(s) é(são): ",end="")
for p in principal:
    if p[1] == men:
        print(f"{p[0]}, ", end="")

