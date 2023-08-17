print("Bom dia, boa tarde, boa noite! Este programa vai mostrar o teu escalão caso estejas numa equipa de natação!")
ano = int(input("Em que ano nasceste? "))
idade = 2023 - ano
if idade > 0 and idade <= 9:
    print("MIRIM")
elif idade > 9 and idade <= 14:
    print("INFANTIL")
elif idade >= 15 and idade <= 19:
    print("JÚNIOR")
elif idade == 20:
    print("SÉNIOR")
elif idade > 20 and idade <= 80:
    print("MASTER")
else:
    print("\033[31m Erro, tenta outra vez \033[m")