# Faça um programa que leia nome e peso de várias pessoas,                                      guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
temp = []
princ = []

while True:
    temp.append(str(input('Nome: ')))
    temp.append(str(input(('Peso: '))))

    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] < men:
            men = temp[1]
        if temp[1] > mai:
            mai = temp[1]

    princ.append(temp[:])
    temp.clear()

    continuar = str(input("Quer continuar? [s/n]\n")).strip()[0]

    if continuar not in 'Ss':
        print('\nVocê não digitou S\n')
        break

# print(f'Os dados foram: {princ}')
print(f'Ao todo você tem {len(princ)} pessoas')
print(f'O menor peso foi de {men}kg, da pessoa ', end='')
for p in princ:
    if p[1] == men:
        print(f'{p[0]}')
print(f'O maior peso foi de {mai}kg, da pessoa ', end='')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]}', end= '')