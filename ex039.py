# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
# do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_nasc = int(input("Digite o ano de nascimento do jovem:\n"))

sexo = str(input("Digite o sexo do jovem. Se for feminino, digite F, se for masculino, digite M:\n"))

ano_atual = date.today().year

idade = ano_atual - ano_nasc

if sexo.lower() == 'f':
    print("Você é mulher, portanto, não precisa fazer o alistamento obrigatório\n")
else:
    if idade > 18:
        saldo = idade-18
        print(f"Você tem {idade} já deveria ter se alistado há {saldo} anos, em {ano_atual-saldo}")
    elif idade < 18:
        saldo = 18-idade
        print(f"Você ainda tem {idade} anos, faltam {saldo} para você se alistar, você irá se alistar em {ano_atual+saldo}")
    else:
        print(f"Você tem {idade} anos, portanto, precisa se alistar este ano!")