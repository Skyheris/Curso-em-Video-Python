import random

print("Olá!! Este programa é um jogo de jokenpô, espero que ganhes ehehe, boa sorte!!")
escolhas = ["Pedra", "Papel", "Tesoura"]
computador = random.choice(escolhas)
jogador = str(input("Pedra, Papel ou Tesoura? "))
if computador == "Pedra" and jogador == "Tesoura":
    print("Perdeste! Tenta outra vez!")
elif computador == "Pedra" and jogador == "Pedra":
    print("EMPATE!")
elif computador == "Pedra" and jogador == "Papel":
    print("GANHASTE! PARABÉNS!")
elif computador == "Tesoura" and jogador == "Pedra":
    print("GANHASTE! PARABÉNS!")
elif computador == "Tesoura" and jogador == "Papel":
    print("Perdeste! Tenta outra vez!")
elif computador == "Tesoura" and jogador == "Tesoura":
    print("EMPATE!")
elif computador == "Papel" and jogador == "Tesoura":
    print("GANHASTE! PARABÉNS!")
elif computador == "Papel" and jogador == "Pedra":
    print("Perdeste! Tenta outra vez!")
elif computador == "Papel" and jogador == "Papel":
    print("EMPATE!")
print("Obrigado por jogares!!")