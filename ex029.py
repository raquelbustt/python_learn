# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

km = float(input("Qual é a velocidade do carro?\n"))

if km > 80:
    multa = (km - 80) * 7
    print(f"Você foi multado! Sua multa custou R${multa}")
else:
    print("Pode prosseguir! Dirija com segurança")