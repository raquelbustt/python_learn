# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input("Digite um numero inteiro:\n"))

print("Escolha para qual base você deseja converter:\n"
      "1 - Converter para Binário\n"
      "2 - Converter para Octal\n"
      "3- Converter para Hexadecimal\n")

opcao = int(input("Sua opção:\n"))

if opcao == 1:
    print(f"O numero {num} convertido para binário é igual a {bin(num)[2:]}")
elif opcao == 2:
    print(f"O numero {num} convertido para octal é igual a {oct(num)[2:]}")
elif opcao == 3:
    print(f"O numero {num} convertido para hexadecimal é igual a {hex(num)[2:]}")
else:
    print("Opção inválida!")