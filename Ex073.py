clubes = ("Botafogo", "Palmeiras", "Flamengo", "Fluminense", "Grêmio", "Red Bull Brigantino", "Atheletico PR", "Fortaleza",
          "Cuiabá-MT", "São Paulo", "Atlético-MG", "Cruzeiro", "Corinthians", "Internacional", "Goiás", "Bahia", "Santos",
          "Vasco da Gama", "Coritiba", "América-MG")
clubes_ordenados = ""
print("Os primeiros 5 colocados são:")
for cont in range(0, len(clubes)):
    if cont < 5:
        print(f"Clube {clubes[cont]}")
print("-"*30)
print("Os últimos 4 colocados são:")
for cont in range(0, len(clubes)):
    if cont >= 16:
        print(f"Clube {clubes[cont]}")
for cont in range(0, len(clubes)):
   clubes_ordenados = tuple(sorted(clubes))
print("-"*30)
print("Os clubes por ordem alfabética são:")
print(clubes_ordenados)


