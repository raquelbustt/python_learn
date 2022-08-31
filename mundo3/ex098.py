# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}: ')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end='  ')
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end='  ')
            cont -= p
        print('FIM!')

inicio = int(input("Digite o valor de início: "))
fim = int(input("Digite o valor de fim: "))
passo = int(input("Digite o valor de passo: "))

while inicio < 0 or fim < 0 or passo <=0:
    print("Você digitou um valor negativo ou decimal! Faça novamente:")

    inicio = int(input("Digite o valor de início: "))
    fim = int(input("Digite o valor de fim: "))
    passo = int(input("Digite o valor de passo: "))

contador(inicio, fim, passo)
