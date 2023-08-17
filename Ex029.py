import random
v = random.uniform(50 , 100)
multa = (v - 80) * 7
if v >= 80:
    print(f"Conduzias a uma velocidade de {v:.2f}km/h, \n por isso tens de pagar uma multa de {multa:.2f}€")
else:
    print("Estás dentro das conformidades da lei, podes seguir")
