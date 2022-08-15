# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

contagem = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', \
            'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',
            'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
opcao = 'S'

while opcao in "Ss":
    n = int(input("Digite um número entre 0 e 20:\n"))

    if 0 > n or n >= 21:
        print("Número inválido, tente novamente mais tarde")
        break

    print(f'Você digitou o número {contagem[n].upper()}\n')

    opcao = str(input("Deseja continuar? [S/N]\n")).strip()[0]