# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - Nome com todas as letras maiúsculas
# - Nome com todas as letras minúsculas
# - Quantas letras sem espaço
# - Quantas letras tem o primeiro nome

nome = str(input("Digite um nome completo\n")).strip()

print(nome)

print("Nome em maiusculo:", nome.upper())

print("Nome em minusculo:", nome.lower())

print("Quantidade de letras:", len(nome) - nome.count(' '))

print("Primeiro nome:", nome.find(' '))

separa = nome.split()

print(f"Seu primeiro nome é {separa[0]} e seu tamanho é {len(separa[0])}")