print("---Analisador de Expressões!---")
expressao = str(input("Digita uma expressão Matemática: "))
parenteses_esquerdos = expressao.count("(")
parenteses_direitos = expressao.count(")")
if expressao.count("(") == expressao.count(")"):
    print("A expressão é válida!")
else:
    print("A expressão é inválida!")
if expressao.count("(") > expressao.count(")"):
    print(f"Falta-te fechar {parenteses_esquerdos - parenteses_direitos} parênteses!")
elif expressao.count("(") < expressao.count(")"):
    print(f"Falta-te abrir {parenteses_direitos - parenteses_esquerdos} parênteses!")
