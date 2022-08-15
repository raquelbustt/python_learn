# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print("*="*20)
print("Analisando triângulos")
print("=*"*20)
lado1 = float(input("Digite o primeiro valor\n"))
lado2 = float(input("Digite o segundo valor\n"))
lado3 = float(input("Digite o terceiro valor\n"))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("É possível fazer um triângulo com essas retas!!")
else:
    print("Não é possível fazer um triângulo com essas retas!!")