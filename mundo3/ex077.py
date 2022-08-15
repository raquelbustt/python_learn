# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tupla = ('dia', 'noite', 'sol', 'lua')

for i in tupla:

    print(f'\nA palavra {i.upper()} possui as vogais')

    for letra in i:
        if letra.lower() in 'aeiou':
            print(f'{letra:^10}')

    print(30*'-')