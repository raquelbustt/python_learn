# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma_par = soma_coluna = maior= 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valor para a posição [{l}, {c}]: "))

        if matriz[l][c] % 2 ==0:
            soma_par += matriz[l][c]

        if matriz[l][2]:
            soma_coluna += matriz[l][2]

        if c == 0 or matriz[1][c] > maior:
            maior = matriz[1][c]

for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f"A soma dos pares é: {soma_par}")
print(f"A soma da terceira coluna é: {soma_coluna}")
print(f"A soma da segunda linha é: {maior}")