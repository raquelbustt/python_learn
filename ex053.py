# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input("Digite uma frase\n"))

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
inverso = junto[::-1]

# for letra in range(len(junto)-1, -1, -1):
#     inverso += junto[letra]
print(f"O inverso de {junto} é {inverso}")
if inverso == junto:
    print("Temos um palídromo")
else:
    print("A frase digitada não é um palíndromo")