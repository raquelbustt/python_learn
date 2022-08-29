# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
continuar = 'S'
listanum = []

while True:
    if continuar in 'Ss':
        num = int(input('Digite um valor inteiro\n'))
        if num not in listanum:
            listanum.append(num)
        else:
            print('-' * 30)
            print('O VALOR JÁ CONSTA NA LISTA!!!')
            print('-' * 30)

        continuar = str(input("Quer continuar? [S/N]\n")).strip()[0]

    else:
        print('\nVocê não digitou S\n')
        break

listanum.sort()
print(f'O resultado da sua lista é: {listanum}')
print('Obrigada por utilizar este programa! =)')