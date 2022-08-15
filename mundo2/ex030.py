# Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = float(input("Digite um numero\n"))

if num % 2 == 0:
    print(f"O número {num} é par")
else:
    print(f"O número {num} é impar")