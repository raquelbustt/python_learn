# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = {}

aluno['Nome'] = str(input("Digite o nome: "))
aluno['Média'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno["média"] >= 7:
    aluno["Situação"] = 'Aprovado'
elif aluno["média"] < 7:
    aluno["Situação"] = 'Recuperação'
else:
    aluno["Situação"] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k}: {v}')