# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando
# a estrutura while.

print("======= 10 TERMOS DE UMA PA =======")

primeiro = int(input("Digite o primeiro termo\n"))
razao = int(input("Digite a razão\n"))
termo = primeiro
cont =1

while cont <= 10:
    print(f'{termo}-> ', end='')
    termo += razao
    cont += 1
print('FIM')