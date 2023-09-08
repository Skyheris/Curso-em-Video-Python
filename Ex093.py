print("-="*7)
print("---FUTEBOL---")
print("-="*7)
informacao = {}
informacao['jogador'] = str(input("Nome do Jogador: "))
informacao['partidas'] = int(input("Número de Partidas: "))
if informacao['partidas'] > 0:
    informacao['golos'] = int(input("Número de golos por partida: "))

print(f"O nome do Jogador é {informacao['jogador']}.")

if informacao['partidas'] > 0:
    golos = informacao['golos'] * informacao['partidas']
    informacao['golos_totais'] = golos
    print(f"{informacao['jogador']} jogou {informacao['partidas']} partidas e fez {informacao['golos']} golos por partida.")
    print(f"No total o jogador fez {informacao['golos_totais']} golos.")
else:
    print("O(A) não participou em nenhuma partida!")
print("-"*20)
print("Dados registados com sucesso!")