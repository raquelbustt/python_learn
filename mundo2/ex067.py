# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

n = 0
cont = 0
while True:
    n = int(input("Digite o numero que voce quer ver a tabuada\n"))
    if n < 0:
        break
    while cont != 11:
        print(f'{n} x {cont} = {n * cont}')
        cont += 1
    # for c in range (1, 11):
    #     print(f'{n} x {c} = {n*c}')

print("Programa de tabuada finalizado")