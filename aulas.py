# ----------------- AULA 06 --------------

# n1 = int(input("Digite um valor\n"))
#
# n2 = int(input("Digite outro valor\n"))
#
# s = n1+n2
#
# print(f"A soma entre {n1} e {n2} vale {s}")

# ----------------- AULA 07 --------------

# divisao inteira
# print(5//2)
#
# # resto da divisao
# print(5%2)
#
# # divisao
# print(5/2)
#
# n1 = int(input("Digite um valor\n"))
#
# n2 = int(input("Digite outro valor\n"))
#
# print(f"A soma entre {n1} e {n2} vale {n1+n2}")

# ----------------- AULA 08 --------------
#
#
# import math
#
# num = int(input('Digite um número: \n'))
#
# raiz = math.sqrt(num)
#
# print(f"Raiz: {raiz}")

# ----------------- AULA 09 --------------

# frase = "Curso em vídeo Python"
#
# # Funcionalidades:
#
# print(frase.find('Android'))
#
# # Operador "in"
#
# print('Curso' in frase)
#
# # Transformação não é possivel mexer direto nos elementos de lista
# # mas é possivel fazer isso com métodos
#
# print(frase.replace('Python', 'Android'))
#
# print(frase.upper())
#
# print(frase.lower())
#
# print(frase.capitalize())
#
# print(frase.title())
#
# # frase = '   Aprenda Python   '
#
# print(frase)
#
# print('Remove todos os espaços inúteis:', frase.strip())
#
# frase2 = frase.split()
#
# print(frase2[2][3])
#
# print(frase.count())

# # ----------------- AULA 10 --------------
#
# nome = str(input("Qual seu nome?\n"))
# if nome == "Raquel":
#     print("Que nome lindo você tem!")
# else:
#     print("Seu nome é comum")
# print(f"Bom dia, {nome}")

# ----------------- AULA 12 --------------

# nome = str(input("Qual seu nome?\n"))
# if nome == "Raquel":
#     print("Que nome lindo você tem!")
# elif nome == 'Pedro' or nome == "João" or nome == "Paulo":
#     print("Seu nome é bem comum")
# elif nome in "Ana Cláudia Jéssica Juliana Fabi":
#     print("Seu nome é feminino")
# print(f"Bom dia, {nome}")

# ----------------- AULA 13 --------------
#
# print("primeiro for:")
# for c in range (1, 7):
#     print(c)
#
# print("segundo for:")
# for c in range (7, 0, -1):
#     print(c)
#
# print("terceiro for:")
# for c in range (1, 7, 2):
#     print(c)

# ----------------- AULA 15 ------------

# cont = 1
#
# while cont <= 10:
#     print(cont, '... ', end='')
#     cont += 1
# print(' Acabou')
#
# n = s = 0
#
# while True:
#     n = int(input("Digite um numero\n"))
#     if n == 999:
#         break
#     s += n
#
# print(f"A soma é {s}")