# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos
# em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
partidas = []

jogador['Nome'] = str(input("Digite o nome: "))
total = int(input(f'Quantas partidas o jogador {jogador["Nome"]} jogou? '))

for c in range(0, total):
    partidas.append(int(input(f"Quantos gols na partida {c+1}? ")))

jogador["Gols"] = partidas[:]
jogador["Total de Gols"] = sum(partidas)

print('='*30)

print(f'Jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas')
for i, v in enumerate(jogador["Gols"]):
    print(f'   => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {total} gols.')
# for k, v in jogador.items():
#     print(f'{k}: {v}')