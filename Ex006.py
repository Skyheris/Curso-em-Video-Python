n = int(input("Digita um número inteiro: "))
print ("O dobro de \033[4;31m{}\033[m é \033[34m{}\033[m, o seu triplo é \033[35m{}\033[m e a sua raiz quadrada é \033[33m{:.1f}\033[m".format(n, n*2, n*3, n**(1/2)))
