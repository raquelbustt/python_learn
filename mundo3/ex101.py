# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto (ano):
    from datetime import date

    atual = date.today().year
    idade = atual - ano

    if 16 <= idade < 18 or idade < 65:
        return(f"Essa pessoa tem {idade} anos e o seu voto é OPCIONAL")

    if idade <16:
        return(f"Essa pessoa tem {idade} anos portanto, seu voto foi NEGADO")

    else:
        return(f"Essa pessoa tem {idade} anos e o seu voto é OBRIGATÓRIO")

age = int(input("Digite o ano de nascimento: "))

print(voto(age))