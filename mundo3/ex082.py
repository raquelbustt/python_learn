# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que
# vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo
# das três listas geradas.

continuar = 'S'
listanum = []
listapar = []
listaimpar = []

while True:
    if continuar in 'Ss':
        num = int(input('Digite um valor inteiro\n'))

        listanum.append(num)

        if num % 2 == 0:
            listapar.append(num)
        else:
            listaimpar.append(num)

        continuar = str(input("Quer continuar? [s/n]\n")).strip()[0]

    else:
        print('\nVocê não digitou S\n')
        break

print(f'Sua lista completa = {listanum}')
print(f'Sua lista de numeros pares = {listapar}')
print(f'Sua lista de numeros impares = {listaimpar}')