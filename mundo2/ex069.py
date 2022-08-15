# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#
# A) quantas pessoas tem mais de 18 anos.
#
# B) quantos homens foram cadastrados.
#
# C) quantas mulheres tem menos de 20 anos.

opcao = ' '
tot_maior = tot_homem = tot_mulher = 0
sexo = ' '

while opcao not in "Nn":
    print("="*15, "Tela de cadastro", "="*15)
    idade = int(input("Digite a idade\n"))
    sexo = str(input("Digite o sexo [F/M]\n")).upper().strip()[0]

    if idade >=18:
        tot_maior += 1
    if sexo == 'M':
        tot_homem += 1
    if sexo == 'F' and idade < 20:
        tot_mulher += 1
        
    opcao = str(input("Quer continuar? [S/N]\n")).strip()[0]

print(f"Total de pessoas de maior = {tot_maior}")
print(f"Total de homens = {tot_homem}")
print(f"Total de mulheres com menos de 20 anos = {tot_mulher}")