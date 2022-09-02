# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
# quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum
# dado não tenha sido informado corretamente.

def ficha(nome='DESCONHECIDO', gols=0):

    return f'O jogador(a) {nome} fez {gols} gols'


n = str(input("Digite o nome do jogador: "))
g = str(input("Numero de gols: "))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    print(ficha(gols=g))
else:
    print(ficha(n, g))
