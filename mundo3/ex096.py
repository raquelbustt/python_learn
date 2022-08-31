# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

def area (l, c):
    a = l * c
    print(f'A área do seu terreno é de {a}m^2')


l = float(input("Digite a largura do terreno: "))
c = float(input("Digite o comprimento do terreno: "))
area(l, c)