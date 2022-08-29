# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

continuar = 'S'
listanum = []

while True:
    if continuar in 'Ss':
        listanum.append(int(input('Digite um valor inteiro\n')))

        continuar = str(input("Quer continuar? [s/n]\n")).strip()[0]

    else:
        print('\nVocê não digitou S\n')
        break

listanum.reverse()
print(f'Sua lista possui {len(listanum)} na sua lista '
      f'\nCom os seguintes valores em ordem decrescente: {listanum}')
print(f'O valor 5 está na lista, na posição {listanum.index(5)}') if 5 in listanum else print('Essa lista não possui o valor 5')
print('Obrigada por utilizar este programa! =)')