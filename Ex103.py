def ficha(nome, golos):
    nome = str(input("Digite o nome do jogador: "))
    golos = int(input(f"Total de golos do {nome}: "))
    print("-="*15)
    print(f"O nome do jogador é {nome}")
    if golos > 0:
        print(f"O jogador {nome} marcou {golos} golos")
    else:
        print(f"O jogador {nome} não marcou golos!")


ficha(nome = "", golos = 0)