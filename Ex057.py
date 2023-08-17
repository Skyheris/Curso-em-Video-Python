print("Bem vindos ao detetor de género!!")
sexo = input("Digita o género [M/F]: ")
if sexo.upper().strip() == "M" or sexo.upper().strip() == "F":
    print("Fim!")
else:
    sexo = input("Dados inválidos, digita novamente: ")
print("Obrigado! O sexo registado foi: {}".format(sexo))
