# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa
# tem que analisar todos os valores e dizer qual deles é o maior.

def maior (*num):
    cont = maior = 0

    print(f'\nOs valores passados foram: ')
    for n in num:
        print(f'{n} ', end='')

        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1

    print(f"\nForam informados {len(num)} valores e o maior valor informado foi {maior}")

maior(1, 2, 3, 4, 5)
maior(9,8,7,10)