# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer.

from random import randint

num_comp = randint(0,10)

num_jog = int(input("Digite um número de 0 a 10:\n"))

while num_jog != num_comp:
    num_jog = int(input("\n----- O computador ganhou!!! -----\nMas você pode tentar novamente. \n\nDigite um número de 0 a 10:\n"))

print("-*-*-*- Ufa! Você ganhou! -*-*-*-")