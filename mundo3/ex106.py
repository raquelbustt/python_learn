# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
# Importante: use cores.

def ajuda(com):
    help(com)

def título(msg, cor=0):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')


comando = ''

while True:
    comando = str(input("Função ou biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)