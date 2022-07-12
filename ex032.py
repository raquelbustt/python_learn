# Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
#
ano = int(input("Digite um ano\n"))

# Utilizando operador alternário

bissexto = print(f"O ano {ano} é bissexto") if ano % 4 == 0  and ano % 100 != 0 or ano % 400 == 0 \
    else print(f"O ano {ano} não é bissexto")
