# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando
# ele disser que quer mostrar 0 termos.

print("======= TERMOS DE UMA PA =======")

primeiro = int(input("Digite o primeiro termo\n"))
razao = int(input("Digite a razão\n"))
termo = primeiro
cont =1
mais = 10
total = 0

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo}-> ', end='')
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos voce quer colocar a mais?\n"))
print('FIM')

