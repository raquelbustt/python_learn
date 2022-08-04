# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores.
from datetime import date

atual = date.today().year

maior = menor = 0

for i in range (1,8):
    ano = int(input(f"Em que ano a pessoa {i} nasceu?\n"))
    idade = atual - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print(f"A quantidade de pessoas de maior é {maior} e a quantidade de pessoas de menor é {menor}.")