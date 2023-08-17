km = float(input("Digita o número de kilómetros que percorreste: "))
dias = int(input("Digita o número de dias em que o carro esteve alugado: "))
pkm = km*0.15
pdias= dias*60
print(f"Como alugaste o carro por {dias} dias e andaste {km}km com ele, vais ter de pagar {pkm+pdias}€")