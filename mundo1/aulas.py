# ----------------- AULA 06 --------------

n1 = int(input("Digite um valor\n"))

n2 = int(input("Digite outro valor\n"))

s = n1+n2

print(f"A soma entre {n1} e {n2} vale {s}")

# ----------------- AULA 07 --------------

# divisao inteira
print(5//2)

# resto da divisao
print(5%2)

# divisao
print(5/2)

n1 = int(input("Digite um valor\n"))

n2 = int(input("Digite outro valor\n"))

print(f"A soma entre {n1} e {n2} vale {n1+n2}")

# ----------------- AULA 08 --------------


import math

num = int(input('Digite um número: \n'))

raiz = math.sqrt(num)

print(f"Raiz: {raiz}")

# ----------------- AULA 09 --------------

frase = "Curso em vídeo Python"

# Funcionalidades:

print(frase.find('Android'))

# Operador "in"

print('Curso' in frase)

# Transformação não é possivel mexer direto nos elementos de lista
# mas é possivel fazer isso com métodos

print(frase.replace('Python', 'Android'))

print(frase.upper())

print(frase.lower())

print(frase.capitalize())

print(frase.title())

# frase = '   Aprenda Python   '

print(frase)

print('Remove todos os espaços inúteis:', frase.strip())

frase2 = frase.split()

print(frase2[2][3])

print(frase.count())
