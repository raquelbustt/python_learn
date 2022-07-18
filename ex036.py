# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

vlr_casa = float(input("Digite o valor da casa: \n"))

vlr_salario = float(input("Digite o valor do salário: \n"))

anos = int(input("Digite em quantos anos o comprador vai pagar: \n"))

prestacao_mes = vlr_casa/(anos*12)

print(f"\nPara pagar R${vlr_casa:.2f} em {anos}, o valor da prestação será de R${prestacao_mes:.2f}\n")

print("Emprestimo negado!") if prestacao_mes > (vlr_salario * 0.3) else print("Emprestimo aprovado!")