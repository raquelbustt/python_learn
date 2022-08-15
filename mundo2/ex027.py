# Crie um programa que leia o nome completo de uma pessoa e mostre mostrando em seguida o primeiro e o ultimo nome separadamente
# Ex: Ana Maria de Souza
# primeiro = Ana
# segundo = Souza

nome = str(input("Digite um nome completo\n"))

separa = nome.split()

print(f"Seu primeiro nome é {separa[0]} e seu ultimo nome é {separa[-1]}")