import random

n1 = input("Primeiro aluno: \n")
n2 = input("Segundo aluno: \n")
n3 = input("Terceiro aluno: \n")
n4 = input("Quarto aluno: \n")

lista = [n1, n2, n3, n4]
random.shuffle(lista)

print('A ordem de apresentação será: \n', lista)