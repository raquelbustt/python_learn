# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
# ou não. No final, mostre:
#
# A) qual é o total gasto na compra.
#
# B) quantos produtos custam mais de R$1000.
#
# C) qual é o nome do produto mais barato.

opcao = menor_nome = ' '
nome_prod = ' '
preco = total_compra = cont_mil = menor = cont = 0

while opcao not in "Nn":
    print("=" * 15, "CADASTRO PRODUTO", "=" * 15)
    nome_prod = str(input("Digite o nome do produto: ")).strip()
    preco = float(input("Digite o preço: R$"))

    # Contar o primeiro registro
    cont += 1

    if cont == 1:
        menor = preco
        menor_nome = nome_prod
    else:
        if preco < menor:
            menor = preco
            menor_nome = nome_prod

    total_compra += preco

    if preco > 1000:
        cont_mil += 1


    opcao = str(input("Quer continuar? [S/N]\n")).strip()[0]


print("*" * 15, "FIM DO PROGRAMA", "*" * 15)

print(f"Total gasto na compra R${total_compra:.2f}")
print(f"Quantidade de produtos de mais de R$1000 = {cont_mil}")
print(f"E o produto mais barato foi {menor_nome}")