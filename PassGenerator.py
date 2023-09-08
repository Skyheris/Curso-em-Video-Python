import random
import time
print("=-"*15)
print("--- GERADOR DE PASSWORDS ---")
print("=-"*15)
escolhas = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz?!#$%&*1234567890@£§€"
quantidade = int(input("Quantos caracteres queres que tenha a tua palavra pass? [1-100]: "))
cont = 0
password = ""
caracter = ""
passwords = []
while True:
    cont = 0
    while True:
        caracter = random.choice(escolhas)
        if caracter not in password:
            password = password + caracter
            cont += 1
        if cont >= quantidade:
            break
    time.sleep(0.3)
    print(f"A password gerada é: {password}")
    passwords.append(password)
    password = ""
    escolha = str(input("Desejas gerar outra password? [S/N]: "))
    if escolha.strip()[0] in "Nn":
        break
    quantidade = int(input("Quantos caracteres queres que tenha a tua palavra pass? [1-100]: "))
print("Finalizando...")
time.sleep(0.6)
print("As passwords geradas foram:")
for i, passe in enumerate(passwords):
    print("-=" * 10)
    time.sleep(0.6)
    print(f"{i + 1}ª password: {passe}")
    time.sleep(0.5)
print("Obrigado por teres utilizado o meu programa!")

