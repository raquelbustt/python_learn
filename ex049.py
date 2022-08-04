# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
num = int(input("Digite um número para ver a sua tabua \n"))

for i in range (0, 11):
    print (f"{num} x {i} = {num*i}")