"""
Ler 3 números e imprimi-los em ordem crescente.

"""
numeros = []
numeros.append(int(input('Digite o primeiro número:')))
numeros.append(int(input('Digite o segundo número:')))
numeros.append(int(input('Digite o terceiro número:')))

numeros.sort()
res = str(numeros)[1:-1]
print('Os números em ordem crescente ficam: ', res)
