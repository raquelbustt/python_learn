# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoas = []
dados_pessoa = {}
soma = media = 0


while True:
    dados_pessoa.clear()

    dados_pessoa['Nome'] = str(input("Digite o nome: ")).title()
    while True:
        dados_pessoa['Sexo'] = str(input("Digite o sexo [F/M]: ")).upper()[0]
        if dados_pessoa['Sexo'] in 'MFmf':
            break
        print("ERRO! Você precisa digitar M ou F!")

    dados_pessoa['Idade'] = int(input("Digite a idade: "))
    soma += dados_pessoa['Idade']

    pessoas.append(dados_pessoa.copy())

    while True:
        continua = str(input("Quer continuar? [S/N] ")).upper()[0]
        if continua in 'SsNn':
            break
        print("ERRO! Você precisa digitar S ou N!")

    if continua in 'Nn':
        break

print(f'Ao toto temos {len(pessoas)} pessoas cadastradas')
media = soma/len(pessoas)
print(f'A média de idade é de {media:.2f} anos')
print(f'As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]}; ', end='')
print(f'\nLista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['Idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print("")
print("FIM DA EXECUÇÃ0")