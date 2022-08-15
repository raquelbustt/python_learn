# Faça um programa que leia um número de 0 a 9999 e mostra na tela cada um dos dígitos separados

num = int(input("Digite um numero\n"))

print("Analisando o numero:", num)

print("Unidade:", num // 1 % 10)

print("Dezena:", num // 10 % 10)

print("Centena:", num // 100 % 10)

print("Milhar:", num // 1000 % 10)