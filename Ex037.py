print("""Boas!! Este programa vai converter um número inteiro, num número \033[31m binário \033[m,
\033[32m octal \033[m, ou \033[33m hexadecimal \033[m. Espero que gostes!""")
# Variáveis
numero = int(input("Digita o número que queres converter: "))
escolha = input("""\033[31m Binário \033[m [ 1 ]
\033[32m Octal \033[m [ 2 ]
\033[33m Hexadecimal \033[m [ 3 ]
Escolhe o formato para que queres converter: """)
# Opções Possíveis
if escolha == "1":
    print("O teu número convertido para \033[31m bin \033[m fica: {}".format(bin(numero) [2:]))
elif escolha == "2":
    print("O teu número convertido para \033[32m oct \033[m fica: {}".format(oct(numero) [2:]))
elif escolha == "3":
    print("O teu número convertido para \033[33m hex \033[m fica: {}".format(hex(numero) [2:]))

