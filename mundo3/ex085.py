# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista
# única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

num = [[], []]
valor = 0

for i in range (1, 8):
    valor = int(input(f"Digite o valor {i}: "))

    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

num[0].sort()
num[1].sort()
print(f"Todos os valores: {num}")
print(f"Valores pares: {num[0]}")
print(f"Valores ímpares: {num[1]}")