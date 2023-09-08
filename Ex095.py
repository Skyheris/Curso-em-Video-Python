print("-="*13)
print("---JOGADORES DAS BOLAS---")
print("-="*13)
perfis = list()
lista_golos = list()
escolha = ""
acumulador = 0

while True:
    perfil = dict()
    golos = 0
    perfil['Nome'] = str(input("Qual o nome do Jogador? "))
    partidas = int(input(f"Quantas partidas jogaste {perfil['Nome']}? "))
    if partidas > 0:
        acumulador = 0
        for c in range(1, partidas + 1):
            golos = int(input(f"Quantos golos marcaste na {c}ª partida? "))
            lista_golos.append(golos)
            perfil['Golos'] = lista_golos.copy()
            acumulador += golos
            perfil['Golos_Totais'] = acumulador
    else:
        golos = 0
        perfil['Golos'] = golos
    perfis.append(perfil.items())
    escolha = str(input("Queres continuar? [S/N]: ")).strip()[0]
    if escolha not in "Ss":
        break
print("Cod  Jogador   Golos    Totais")
for i, valor in enumerate(perfis):
    print(i, end=" ")
    for dado in valor:
        print(f"{str(dado[1]):<12}", end="   ")
    print()












