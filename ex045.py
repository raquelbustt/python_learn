# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print("Opções:\n"
      "0 - Pedra\n"
      "1 - Papel\n"
      "2- Tesoura")

opcao = int(input("Sua opção:\n"))

print(f"Você escolheu {itens[opcao]}")

print(f"O computador escolheu {itens[computador]}")

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(1)

if computador == 0:
      if opcao ==0:
            print("Empate")
      elif opcao == 1:
            print("Jogador venceu")
      elif opcao == 2:
            print("Computador venceu")
      else:
            print("Jogada inválida!")
elif computador == 1:
      if opcao ==0:
            print("Computador venceu")
      elif opcao == 1:
            print("Empate")
      elif opcao == 2:
            print("Jogador venceu")
      else:
            print("Jogada inválida!")
elif computador == 2:
      if opcao ==0:
            print("Jogador venceu")
      elif opcao == 1:
            print("Computador venceu")
      elif opcao == 2:
            print("Empate")
      else:
            print("Jogada inválida!")