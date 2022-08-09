# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

v = 0

while True:
    jogador = int(input("Digite um numero\n"))
    comp = randint(0, 11)
    total = jogador + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input("Par ou impar? [P/I]\n")).upper().strip()[0]
    print(f"Voce jogou {jogador} e o computador {comp}, totalizando {total}")

    if tipo == "P":
        if total % 2 == 0:
            print("Jogador venceu")
            v += 1
        else:
            print("Jogador perdeu")
            break

    print("Vamos jogar novamente")

print(f"O computador venceu! Você venceu {v} vezes")