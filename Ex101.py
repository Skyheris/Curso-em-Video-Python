def voto():
    idade = 2023 - ano
    if idade < 18:
        print(f"Com {idade} anos, não podes votar! Espera mais {18 - idade} anos para votar!")
    elif idade >= 18 and idade < 65:
        print(f"És obrigado a votar pois tens {idade} anos!")
    elif idade >= 65:
        print(f"É opcional votar pois tem mais de 65 anos!")


ano = int(input("Digita o teu ano de nascimento: "))
voto()