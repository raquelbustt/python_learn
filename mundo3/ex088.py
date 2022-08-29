# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos
# jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
cont = 0
jogo = []
qtd_jogos = int(input("Digite quantos jogos serão sorteados? "))
total_jogos = 1

for i in range (0, qtd_jogos):
    while len(jogo) < 6:
        num = randint(0, 60)

        if num not in jogo:
            jogo.append(num)
    print(f'Numeros sorteados do jogo {i}: {jogo}')
    jogo.clear()

#
# while total_jogos <= qtd_jogos:
#     while True:
#         num = randint(0,60)
#
#         if num not in lista:
#             lista.append(num)
#             cont += 1
#         if cont > 6:
#             break
#
#     lista.sort()
#     jogos.append(lista[:])
#     lista.clear()
#     total_jogos += 1
#
# for i, listas in enumerate(jogos):
#     print(f"Os números sorteados do jogo {i} foram: {listas}")