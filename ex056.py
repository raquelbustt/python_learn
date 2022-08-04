# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
# grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

idadetotal = maior_idade_homem = 0
nome_mais_velho = ''
mulher20 = 0

for i in range (1, 5):
    print(f"------ FORMULÁRIO PESSOA {i} ------")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo (M/F): ")).strip()
    idadetotal += idade
    if i == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Ff' and idade > 20:
        mulher20 += 1

print(f"A média de idade é de {idadetotal/4} anos")
print(f"O homem mais velho é o {nome_mais_velho} e sua idade é de {maior_idade_homem} anos.")
print(f"O total de mulheres com mais de 20 anos é igual a {mulher20}")