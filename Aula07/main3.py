"""
Altere o exercicio anterior para que o usuário digite em qual coluna o retangulo irá se formar

"""

coluna = int(input('Digite em qual coluna o retângulo irá se formar:'))
largura = int(input('Digite a largura do retângulo:'))
espaco = ' '
for i in range(10):
    print(espaco*coluna+'#'*largura)

