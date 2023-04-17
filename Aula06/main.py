"""
Faça um algoritmo que leia o nome e o salário de 5 pessoas. Após a digitação,
mostre o nome e o salário da pessoa que recebe o menor salário.

Obs. Crie uma solução sem o uso de listas.
"""

dados = {}
nomeMenor = 0
salarioMenor = 0
i = 0
while i != 5:
    nome = input('Digite seu nome:')
    salario = float(input('Digite seu salário:'))
    i = i + 1
    dados[nome] = salario

for dado in sorted(dados, key = dados.get, reverse=True):
    print(f'Nome = {dado} e Salário = {dados[dado]}')
    valorMenor = dado
    salarioMenor = dados[dado]

print('O menor valor é o de: ', nomeMenor, ' com um salário de:',salarioMenor)
