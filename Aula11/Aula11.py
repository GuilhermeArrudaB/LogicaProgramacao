"""
Guilherme Arruda Brito
Matricula 181900281
"""

lst_negativos = []

while True:

    print('"0" encerra o algoritmo.')
    num = int(input('Digite um número: '))
    if num == 0:
        exit()

    if num < 0:
        lst_negativos.append(num)

    if num > 20 and num < 60:
        num2 = int(input('Digite outro número: '))
        if num2 == num:
            print('Não há nenhum número inteiro entre o primeiro e o segundo número')
        elif num2 != num:
            print('Números entre ',num,' e ',num2)
            if num > num2:
                for numero in range(num2, num):
                    print(numero, end=',')
            for numero in range(num, num2):
                print(numero, end=',')
        print('\n')

    if num > 40 and num < 80:
        num3 = int(input('Digite outro número: '))
        if num3 > num:
            print('Números inteiros e pares entre :',num3,' e ',num)
            for numero2 in range(num3, num, -1):
                if numero2 %2 == 0:
                    print(numero2, end=',')
        else:
            print('Números inteiros e pares entre :',num,' e ',num3)
            for numero2 in range(num, num3, -1):
                if numero2 %2 == 0:
                    print(numero2, end=',')

    if num < 20 or num > 80:
        if num > 0:
            print('Número OK')

    print('\n')
    if len(lst_negativos) != 0:
        print('O menor número negativo =',min(lst_negativos))
        print('O maior número negativo =',max(lst_negativos))
    else:
        print('Nenhum número negativo')
