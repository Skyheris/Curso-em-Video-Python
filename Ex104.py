from time import sleep


def leiaint(msg):
    valor = msg
    while True:
        if valor.strip().lstrip("-").isnumeric():
            print(f"Você digitou o valor {int(valor)}")
            break
        else:
            sleep(0.3)
            print("\033[31mERRO! Número Inválido.\033[m")
            valor = input("Digite um número inteiro válido: ")


leiaint(input("Digita um número: "))
