"""
Altere o exercicio anterior para ler mais de um texto, armazenando em uma lista de textos. lst_textos
"""

vogal = []
lst_textos = []

while True:
    texto = input('Digite um texto (fim - encerra): ')
    if texto == 'fim:':
        break
    qt = 0
    lst_textos.append(texto)
    for frase in lst_textos:
        qt += 1
        print('---------------------')
        print(f'A quantidade de letras do {qt} texto é {len(texto)}')
        qt_vogais = 0
        for vogal in ['a','e','i','o','u']:
            qt_vogais += texto.count(vogal)
        print(f'A quantidade de vogais para o {qt} texto é {qt_vogais}')
        
