# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já
# na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []

for i in range (0, 5):
    num = int(input('Digite um valor\n'))

    if i == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado no final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos = pos + 1

print('Resultado da sua lista: ', lista)