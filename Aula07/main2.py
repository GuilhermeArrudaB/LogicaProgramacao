"""
Altere o exercicio anterior para que o usuário digite em qual coluna o retangulo irá se formar

"""

coluna = int(input('Digite em qual coluna o retângulo irá se formar:'))
espaco = ' '
for i in range(10):
    print(espaco*coluna+'#'*10)

