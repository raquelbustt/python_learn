# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N
# primeiros elementos de uma Sequência de Fibonacci.

num = int(input("Quantos termos voce quer mostrar?\n"))

t1 = 0
t2 = 1
print(f"{t1}-> {t2}", end='')
cont = 3
while cont <= num:
    t3 = t1 + t2
    print(f'-> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print("FIM")