# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
#
from datetime import datetime

trabalhador = {}

trabalhador['Nome'] = str(input("Digite o nome: "))
trabalhador['Ano de nascimento'] = int(input(f'Digite o ano de nascimento de {trabalhador["Nome"]}: '))
idade = datetime.now().year - trabalhador['Ano de nascimento']
trabalhador['Carteira de trabalho'] = int(input("Carteira de trabalho (Digite 0 se não tiver): "))

if trabalhador['Carteira de trabalho'] != 0:
    trabalhador['Ano contratação'] = int(input(f'Digite o ano de contratação de {trabalhador["Nome"]}: '))
    trabalhador['Salário'] = float(input("Salário: R$"))
    trabalhador['Aposentadoria'] = trabalhador['Ano contratação'] + 35

print('='*10, "CARTEIRA DE TRABALHO", "="*10)
for k, v in trabalhador.items():
    print(f'{k}: {v}')