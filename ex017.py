import math

opo = float(input("Qual o comprimento do cateto oposto?\n"))

adj = float(input("Qual o comprimento do cateto adjacente?\n"))

# hi = (opo ** 2 + adj ** 2) ** (1/2)

hi = math.hypot(opo, adj)

print(f"A hipotenusa vai medir: {hi:.2f}")