# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de
# um atleta e mostre sua categoria, de acordo com a idade:
#
# – Até 9 anos: MIRIM
#
# – Até 14 anos: INFANTIL
#
# – Até 19 anos: JÚNIOR
#
# – Até 25 anos: SÊNIOR
#
# – Acima de 25 anos: MASTER

from datetime import date

ano_nasc = int(input("Digite o ano de nascimento do(a) nadador(a):\n"))

ano_atual = date.today().year

idade = ano_atual - ano_nasc

print(f"O nadador tem {idade} anos")

if idade <= 9:
    print(f"Logo, sua categoria é MIRIM")
elif idade <= 14:
    print(f"Logo, sua categoria é INFANTIL")
elif idade <= 19:
    print(f"Logo, sua categoria é JUNIOR")
elif idade <= 25:
    print(f"Logo, sua categoria é SENIOR")
elif idade > 25:
    print(f"Logo, sua categoria é MASTER")