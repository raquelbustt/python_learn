# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
from math import factorial

num = int(input("Digite um valor inteiro para calcular seu fatorial\n"))

f = factorial(num)

print(f"O fatorial de {num} é igual a {f}")