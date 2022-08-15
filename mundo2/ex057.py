# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a
# digitação novamente até ter um valor correto.

sexo = str(input("Digite o sexo [M/F]\n")).strip()

while sexo not in 'MmFf':

    sexo = str(input("Opção inválida! \nDigite o sexo [M/F]:\n")).strip()

print(f"Sexo {sexo.upper()} adicionado com sucesso!")
