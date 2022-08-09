# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
# média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário
# se ele quer ou não continuar a digitar valores.

continuar = 'n'
num = soma = cont = menor = maior =0

while continuar != 'S':
    num = int(input("Digite um numero inteiro\n"))

    soma += num
    cont += 1

    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    continuar = str(input("Quer continuar? [S/N]")).upper().strip()[0]

media = soma/cont
print(f"Você digitou {cont} e a média foi de {media}. O menor numero foi {menor} e o maior foi {maior}")