# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "A"
# - Em que posição ela aparece a primeira vez
# - Em que posição ela aparece a ultima vez

frase = input("Digite uma frase\n").lower().strip()
print(frase)

print(f"A letra A aparece na frase {frase.count('a')} vezes")

print(f"A primeira letra A foi encontrada na posição {frase.find('a')+1}")

print(f"A ultima letra A foi encontrada na posição {frase.rfind('a')+1}")