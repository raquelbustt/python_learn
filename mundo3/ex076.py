# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

lista = ('Computador', 3500.00,
            'Monitor', 876.00,
            'Headphone', 239.00,
            'Adaptador', 50.00)

#print(f'------------ PRODUTOS LOJA ------------')
print(f'{"PRODUTOS LOJA":^40}')

for posicao in range(0, len(lista)):
    if posicao % 2 == 0:
        print(f'{lista[posicao]:.<30}', end='')
    else:
        print(f'R${lista[posicao]:>7.2f}')