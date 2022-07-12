# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = float(input("Qual é a distancia da sua viagem em km?\n"))

# Utilizando operador alternário

valor = km * 0.50 if km <= 200 else km * 0.45

# if km < 200:
#     valor = km * 0.50
# else:
#     valor = km * 0.45

print(f"Sua viagem vai custar R${valor}")