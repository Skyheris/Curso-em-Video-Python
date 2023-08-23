print("-"*36)
print("\033[1:35m →BEM VINDO AO SOMADOR DE NÚMEROS← \033[m")
print("\033[1:35m       PARA SAIR DIGITE 999 \033[m")
print("-"*36)
cont = 0
acumulador = 0
numeros = int(input("Digita um valor inteiro: "))
print("-"*36)
while numeros != 999:
    cont = cont + 1
    numeros = int(input("Digita um valor inteiro: "))
    print("-"*36)
    acumulador = acumulador + numeros
valor_apresentado = acumulador - 999
print(f"A soma de todos os números que digitaste é: {valor_apresentado}")


