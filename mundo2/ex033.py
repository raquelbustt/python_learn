# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

valor1 = float(input("Digite o primeiro valor\n"))

valor2 = float(input("Digite o segundo valor\n"))

valor3 = float(input("Digite o terceiro valor\n"))

menor = valor1

if valor2 < valor1 and valor2 < valor3:
    menor = valor2
if valor3 < valor1 and valor3 < valor2:
    menor = valor3

maior = valor1

if valor2 > valor1 and valor2 > valor3:
    maior = valor2
if valor3 > valor1 and valor3 > valor2:
    maior = valor2

print(f"O menor valor digitado foi {menor}")

print(f"O maior valor digitado foi {maior}")

