print("SEQUÊNCIA DE FIBONACCI!")
numtermos = int(input("Quantos termos queres que sejam apresentados? "))
print("-"*30)
cont = 0  # 2 , 2 , 4 , 6 , 10 , 16
termoini = 0
termomed = 1
termodep = 0
print("\033[1:34m{}\033[m → \033[1:34m{}\033[m →".format(termoini, termomed), end=" ")
while cont < numtermos - 2:
    cont = cont + 1
    termodep = termoini + termomed
    termoini = termomed
    termomed = termodep
    print("\033[1:34m{}\033[m".format(termodep), end=" → ")
print("FIM", end="")
