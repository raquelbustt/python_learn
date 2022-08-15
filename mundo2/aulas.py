# # ----------------- AULA 10 --------------
#
nome = str(input("Qual seu nome?\n"))
if nome == "Raquel":
    print("Que nome lindo você tem!")
else:
    print("Seu nome é comum")
print(f"Bom dia, {nome}")

# ----------------- AULA 12 --------------

nome = str(input("Qual seu nome?\n"))
if nome == "Raquel":
    print("Que nome lindo você tem!")
elif nome == 'Pedro' or nome == "João" or nome == "Paulo":
    print("Seu nome é bem comum")
elif nome in "Ana Cláudia Jéssica Juliana Fabi":
    print("Seu nome é feminino")
print(f"Bom dia, {nome}")

# ----------------- AULA 13 --------------

print("primeiro for:")
for c in range (1, 7):
    print(c)

print("segundo for:")
for c in range (7, 0, -1):
    print(c)

print("terceiro for:")
for c in range (1, 7, 2):
    print(c)

# ----------------- AULA 15 ------------

cont = 1

while cont <= 10:
    print(cont, '... ', end='')
    cont += 1
print(' Acabou')

n = s = 0

while True:
    n = int(input("Digite um numero\n"))
    if n == 999:
        break
    s += n

print(f"A soma é {s}")

