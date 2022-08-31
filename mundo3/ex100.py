# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a
# soma entre todos os valores pares sorteados pela função anterior.

from random import randint

def sorteia(lista):

    for cont in range(0,5):
        num = randint(0, 100)
        lista.append(num)
        print(f'{num}  ', end='')

    print('FIM DA LISTA')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista} temos: {soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)