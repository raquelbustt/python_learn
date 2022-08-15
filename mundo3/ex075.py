# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
#
# B) Em que posição foi digitado o primeiro valor 3.
#
# C) Quais foram os números pares.

num = tuple(int(input("Digite um valor inteiro: \n")) for c in range(1,6))

print(f'Voce digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)}x') if 9 in num else print("O valor 9 não foi digitado")
print(f'O valor 3 apareceu na posição {num.index(3)+1}')  if 3 in num else print("O valor 3 não foi digitado")
print('Os valores pares digitados foram: ', end='')

for n in num:
    if n % 2 == 0:
        print(f'{n}, ', end=' ')