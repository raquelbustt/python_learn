# ********************************** MUNDO 3 **********************************

# ----------------- AULA 16 ------------

# lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'
#
# print(lanche[-2])
#
# print(lanche[1:3])
#
# print(lanche[:2])
#
# print(lanche[-3])
#
# for c in lanche:
#     print(f'Eu vou comer {c}')
#
# a = (1,2,3)
# b= (3,4,5)
# c = b+a
#
# print(c)
# print(c.count(3))
# print(c.index(3))

# ----------------- AULA 17 ------------
#
# num = [2,3,4]
# print(num)
#
# num[2] = 9
# print(num)
#
# num.append(7)
# print(num)
#
# num.sort()
# print(num)
#
# num.sort(reverse=True)
# print(num)
#
# print(f'Essa lista possui {len(num)} elementos')
#
# num.insert(0, 0)
# print(num)
#
# num.pop(0)
# print(num)
#
# num.insert(0, 2)
# print(num)
#
# num.remove(2)
# print(num)
#
# valores = list()
# valores.append(5)
# valores.append(7)
# valores.append(3)
#
# for cont in range(0, 3):
#     valores.append(int(input('Digite um valor\n')))
#
# for c, v in enumerate(valores):
#     print(f'Na posicao {c}, temos o valor {v}')

# ----------------- AULA 18 ------------
#
# galera = []
# dado = []
#
# for c in range(0,3):
#     dado.append(str(input('Nome: ')))
#     dado.append(int(input('Idade: ')))
#     galera.append(dado[:])
#     dado.clear()
#
# print(galera)
# totmai = totmen = 0
#
# for p in galera:
#     if p[1] >= 18:
#         print(f'{p[0]} é maior de idade')
#         totmai += 1
#     else:
#         print(f'{p[0]} é menor de idade')
#         totmen +=1
#
# print(f'Temos {totmai} pessoas de maior e {totmen} menor de idade')

# ----------------- AULA 19 ------------

pessoas = {'nome' : 'Gustavo', 'sexo': 'm', 'idade': 22}

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

print(pessoas.items())

pessoas['peso'] = 98.5

for k, v in pessoas.items():
    print(f'{k} = {v}')


estado1 = {'uf': 'Rio de Janeiro', 'sigla' : 'RJ'}
estado2 = {'uf': 'Sao Paulo', 'sigla' : 'SP'}

brasil = []

brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[0]['uf'])

estado = {}
brasil = []

for c in range (0,3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input(("Sigla do Estado: ")))
    brasil.append(estado.copy())

print(brasil)

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()