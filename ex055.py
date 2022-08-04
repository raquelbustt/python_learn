# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

peso_maior = peso_menor = 0

for i in range (1, 6):
    peso = float(input(f"Digite o pesso da pessoa {i}\n"))

    if i == 1:
        peso_maior = peso
        peso_menor = peso
    else:
        if peso > peso_maior:
            peso_maior = peso
        if peso < peso_menor:
            peso_menor = peso

print(f"O menor peso foi de {peso_menor}kg")
print(f"E o maior peso foi de {peso_maior}kg")