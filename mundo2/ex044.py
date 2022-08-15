#Elabore um programa que calcule o valor a ser pago por um
# produto, considerando o seu preço normal e condição de pagamento:
#
# – à vista dinheiro/cheque: 10% de desconto
#
# – à vista no cartão: 5% de desconto
#
# – em até 2x no cartão: preço formal
#
# – 3x ou mais no cartão: 20% de juros

preco = float(input("Digite o preço das compras:\n"))

print("Formas de pagamento:\n"
      "1 - A vista dinheiro/chque\n"
      "2 - A vista no cartão\n"
      "3- Em até 2x no cartão\n"
      "4- Em 3x ou mais no cartão")

opcao = int(input("Sua opção:\n"))

if opcao == 1:
    pagamento = preco - (preco*0.1)
    print(f"Sua compra de R${preco:.2f} ficará no total de R${pagamento:.2f}")
elif opcao == 2:
    pagamento = preco - (preco * 0.05)
    print(f"Sua compra de R${preco:.2f} ficará no total de R${pagamento:.2f}")
elif opcao == 3:
    pagamento = preco
    print(f"Sua compra de R${preco:.2f} ficará no total de R${pagamento:.2f}")
elif opcao == 4:
    pagamento = preco + (preco*0.2)
    print(f"Sua compra de R${preco:.2f} ficará no total de R${pagamento:.2f}")
else:
    print("Opção inválida!")