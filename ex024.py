# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = input("Digite o nome da cidade\n").strip()

print(cidade[:5].upper().find('SANTO'))