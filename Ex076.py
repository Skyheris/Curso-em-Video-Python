listagem= ("Massa", 0.65, "Leite", 0.70, "Pão", 1.50, "Água", 1.33, "Café", 7.88, "Manteiga", 2.69)
print("-"*8, "Lista de preços", "-"*8)
for cont in range(0, len(listagem)):
    if cont % 2 == 0:
        print(f"\033[1m{listagem[cont]}", "." *(30 - (len(listagem[cont]))), f"{listagem[cont + 1]:.2f}€\033[m")
print("-"*37)