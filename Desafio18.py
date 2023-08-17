import math
ang = float(input("Digita um ângulo em graus: "))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print(f" O seno é {seno:.2f} \n O cosseno é {cosseno:.2f} \n A tangente é {tangente:.2f}")