# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input("Digite um número inteiro \n"))
tot = 0

for i in range(1, num +1):
    if num % i == 0:
        tot += 1
        # print(f"{i}", end = " ")

print (f"O numero {num} foi divisivel {tot} vezes")

if tot == 2:
    print(f"O numero {num} é primo")
else:
    print(f"O numero {num} não é primo")