"""
Faça um algoritmo que leia um texto e mostre
a quantidade de caracteres digitados e
quantas vogais existem neste texto.
obs. Considerar somente as vogais (aeiouAEIOU)

"""
vogal = []
texto = input('Digite um texto:')
textoTamanho = len(texto)

for letra in texto.lower():
    if letra in 'aeiou':
        vogal.append(letra)

print('O texto tem ',textoTamanho,' caracteres de tamanho e ',vogal,' vogais')

