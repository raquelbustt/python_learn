# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
#
# – Média abaixo de 5.0: REPROVADO
#
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
#
# – Média 7.0 ou superior: APROVADO

nota1 = float(input("Digite a primeira nota:\n"))

nota2 = float(input("Digite a segunda nota:\n"))

media = (nota2+nota1)/2

if media < 5:
    print(f"A média foi de {media:.2f}, portanto, o aluno foi REPROVADO!")
elif media >= 5 and media < 7:
    print(f"A média foi de {media:.2f}, portanto, o aluno está de RECUPERAÇÃO!")
else:
    print(f"A média foi de {media}, portanto, o aluno foi APROVADO!")