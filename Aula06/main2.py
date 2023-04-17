"""
Faça um algoritmo que leia vários nomes e salários. Após a digitação,
mostre o nome e o salário da pessoa que recebe o menor salário.

Obs. Crie uma solução sem o uso de listas.
"""
i = 0
digitacao1 = True
while i != 1:
    nome = input('Nome:')
    salario = float(input('Salário:'))
    if digitacao1 == True or salario < menor_salario:
        menor_salario = salario
        nome_menor_sal = nome
        digitacao1 = False
    print('Deseja sair?')
    i = int(input('1 - Sim 2 - Não: '))

print('Menor salário:', menor_salario)
print('Nome da pessoa:',nome_menor_sal)
