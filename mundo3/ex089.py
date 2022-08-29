# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
# notas de cada aluno individualmente.

boletim = []
lista_i = []
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1+nota2)/2

    boletim.append([nome, [nota1, nota2], media])

    continuar = str(input("Quer continuar? [N/S]\n"))

    if continuar not in 'Ss':
        break

print(boletim)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')

for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')


while True:
    opc = int(input("Mostrar notas de qual aluno?\n"))


    if opc in lista_i:
        print(f"As notas de {a[opc][0]} são: {a[opc][1]}")

    opc = False