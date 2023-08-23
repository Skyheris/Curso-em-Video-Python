print("---Identificador de Vogais!---")
palavras = ("Curso", "Aula", "Python", "Video", "Rato", "Jogos", "Estudar")
vogais = "aeiou"
for p in palavras:
    print(f"\nNa palavra {p} temos as vogais: ", end=(""))
    for letra in p:
        if letra.lower() in vogais:
            print(letra.lower(), end=(""))
