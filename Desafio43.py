print("Bem vindo(a)!! Este programa vai calcular o teu IMC com base na tua altura e no teu peso!")
peso = float(input("Digita o teu peso em kg: "))
altura = float(input("Qual é a tua altura em metros? "))
imc = peso / altura**2
if imc > 0 and imc <= 18.5:
    print("Estás abaixo do peso, precisas de comer mais!!!")
elif imc > 18.5 and imc <= 25:
    print("O teu peso está ideal!! PARABÉNS!")
elif imc > 25 and imc <= 30:
    print("Estás em sobrepeso, tenta repensar a tua alimentação!")
elif imc > 30 and imc <= 40:
    print("Estás num estado de obesidade!!! CUIDADO!! Pode fazer mal à tua saúde!!")
elif imc > 40 and imc < 100:
    print("Estás num estado de obesidade mórbida!!! Vai já tratar da tua saúde!! URGENTE!!!")
print("Agora já sabes qual é o teu IMC, {:.1f} , não tens de quê :)".format(imc))