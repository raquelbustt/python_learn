# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

print("======= 10 TERMOS DE UMA PA =======")

termo = int(input("Digite o primeiro termo\n"))
razao = int(input("Digite a razão\n"))
decimo = termo + (10 - 1) * razao

for i in range (termo, decimo + razao, razao):
    print(f"{i}", end ="-> ")
print("FIM")