# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#
# – IMC abaixo de 18,5: Abaixo do Peso
#
# – Entre 18,5 e 25: Peso Ideal
#
# – 25 até 30: Sobrepeso
#
# – 30 até 40: Obesidade
#
# – Acima de 40: Obesidade Mórbida

peso = float(input("Digite o peso da pessoa:\n"))

altura = float(input("Digite a altura da pessoa:\n"))

imc = peso / (altura ** 2)

print(f"Sua altura é {altura:.2f}, seu peso é {peso:.2f} e seu IMC é {imc:.2f}")

if imc < 18.5:
    print("Seu IMC está abaixo do normal!")
elif imc >= 18.5 and imc < 25:
    print("Seu IMC está dentro do normal!")
elif imc >= 25 and imc < 30:
    print("Seu IMC está na faixa de sobrepeso!")
elif imc >= 30 and imc < 40:
    print("Seu IMC está na faixa de obesidade!")
else:
    print("Seu IMC está na faixa de obesidade mórbida! Cuidado!!!")