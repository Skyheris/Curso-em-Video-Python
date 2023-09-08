def fatorial(num):
    """
    Mostra o fatorial de um número à escolha e depois mostra-te
    Primeiro insere o número na função
    Depois a função através de um loop calcula o fatorial
    Depois guarda o resultado e mostra
    """
    resultado = 1

    for c in range(num, 0, -1):
        resultado *= c
    return resultado


num = int(input("Digita o número que queres fatoriorizar: "))

print(f"O fatorial de {num} é {fatorial(num)}")
escolha = str(input("Queres ver como a função funciona? ")).strip()[0]
if escolha in "Ss":
    help(fatorial)
