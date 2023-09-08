import time

temp = list()
notas = list()
nomemedia = list()
tudo = list()
espaco = " "
nomes = list()
while True:
    nome = str(input("Nome do Aluno: "))
    nota1 = float(input("Nota 1 do Aluno: "))
    nota2 = float(input("Nota 2 do Aluno: "))
    media = (nota1 + nota2) / 2
    nomemedia.append(nome)
    nomes.append(nome)
    temp.append(nota1)
    temp.append(nota2)
    nomemedia.append(media)
    notas.append(temp[:])
    tudo.append(nomemedia[:])
    temp.clear()
    nomemedia.clear()
    escolha = str(input("Queres continuar? [S/N]: "))
    if escolha in "Nn":
        break

print("-="*20)
print("Nº  NOME        MÉDIA")
print("-"*25)
for i, nomemedia in enumerate(tudo):
    print(f"{i}  {nomemedia[0]}{espaco*(14-len(nomemedia[0]))}{nomemedia[1]}")
individual = int(input("Desejas mostrar as notas de que aluno? (999 acaba o código): "))
while True:
    if individual == 999:
        break
    print(f"As notas do(a) {nomes[individual]} são {notas[individual]}")
    individual = int(input("Desejas mostrar as notas de que aluno? (999 acaba o código): "))
print("Finalizando o programa", end="")
time.sleep(0.8)
print(".", end="")
time.sleep(0.8)
print(".", end="")
time.sleep(0.8)
print(".", end="")
time.sleep(0.7)
print("\n<<< Volta Sempre >>>")





