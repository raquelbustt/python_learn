# Crie um programa que leia dois valores e mostre um menu na tela:
#
# [ 1 ] somar
#
# [ 2 ] multiplicar
#
# [ 3 ] maior
#
# [ 4 ] novos números
#
# [ 5 ] sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.

num1 = int(input("Digite um valor inteiro\n"))

num2 = int(input("Digite outro valor inteiro\n"))

opcao = 0

while opcao != 5:
    print("----------- MENU -----------\n" \
          "[ 1 ] somar\n" \
          "[ 2 ] multiplicar\n" \
          "[ 3 ] maior\n" \
          "[ 4 ] novos números\n" \
          "[ 5 ] sair do programa")

    opcao = int(input("Digite uma opção\n"))

    if opcao == 1:
        print(f"A soma de {num1} + {num2} = {num1+num2}")
    elif opcao == 2:
        print(f"O produto de {num1} * {num2} = {num1*num2}")
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f"Entre {num1} e {num2}, {maior} é maior")
    elif opcao == 4:
        num1 = int(input("Digite um valor inteiro\n"))
        num2 = int(input("Digite outro valor inteiro\n"))

print("Obrigada por participar do meu menu!")