dictionary = dict()
dictionary['nome'] = str(input("Qual é o nome do aluno? "))
dictionary['média'] = float(input(f"Qual é a média do(a) {dictionary['nome']}? "))
dictionary['situation'] = ""
if dictionary['média'] > 0 and dictionary['média'] < 10:
    dictionary['situation'] = "reprovado(a)"
elif dictionary['média'] >= 10 and dictionary['média'] <= 20:
    dictionary['situation'] = "aprovado(a)"
else:
    print("Erro! Tenta Outra vez!")

print(f"O(A) {dictionary['nome']} tem média de {dictionary['média']} logo está {dictionary['situation']}")