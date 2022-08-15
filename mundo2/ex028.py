#  Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
#  descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

num = randint(0, 5)


num2 = int(input("Digite um número de 0 a 5:\n"))

if num == num2:
    print(f"Parabéns, vc acertou o numero, que é {num}")
else:
    print(f"Ish, vc não acertou o numero, que era {num}. Mais sorte da próxima vez!")