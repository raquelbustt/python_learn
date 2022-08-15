# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#
# – EQUILÁTERO: todos os lados iguais
#
# – ISÓSCELES: dois lados iguais, um diferente
#
# – ESCALENO: todos os lados diferentes

print("*="*20)
print("Analisando triângulos")
print("=*"*20)
lado1 = float(input("Digite o tamanho do primeiro lado:\n"))
lado2 = float(input("Digite o tamanho do segundo lado:\n"))
lado3 = float(input("Digite o tamanho do terceiro lado:\n"))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:

    if lado1 == lado2 == lado3:
        tipo = "EQUILÁTERO"
    elif lado1 != lado2 != lado3 != lado1:
        tipo = "ESCALENO"
    else:
        print("ISÓCELES")

    print(f"É possível fazer um triângulo {tipo} com essas retas!!")
else:
    print("Não é possível fazer um triângulo com essas retas!!")