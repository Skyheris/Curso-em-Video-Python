print("-"*6, "REGISTOS", "-"*6)
idade = int(input("Digita a tua idade: "))
sexo = str(input("Qual o teu sexo? [M/F] ")).upper().strip()[0]
print("-"*20)
cont = 0
homens = 0
mulheres_20 = 0
escolha = ""
while True:
    if idade > 18:
        cont += 1
    elif sexo.upper().strip() == "M":
        homens += 1
    elif sexo.upper().strip() == "F" and idade < 20:
        mulheres_20 += 1
    escolha = str(input("Desejas Continuar? [S/N] "))
    print("-=-" * 10)
    if escolha.upper().strip()[0] == "S":
        idade = int(input("Digita a tua idade: "))
        print("-" * 20)
        sexo = str(input("Qual o teu sexo? [M/F] ")).upper().strip()[0]
    else:
        break
print("-"*20)
print(f"{cont} pessoas têm mais de 18 anos!")
print("-"*20)
print(f"Foram registados {homens} homens!")
print("-"*20)
print(f"Existem {mulheres_20} mulheres com menos de 20 anos")