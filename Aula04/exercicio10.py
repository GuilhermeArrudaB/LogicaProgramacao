"""
Fazer um algoritmo para ler duas notas, os pesos de cada nota e mostrar a média ponderada.
(nota 1 * peso da nota 1) + (nota 2 * peso da nota 2)
Cálculo da Média Ponderada = ------------------------------------------------------------------------
soma dos pesos

"""

nota1 = float(input('Digite sua primeira nota: '))
peso1 = float(input('Digite o peso da primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
peso2 = float(input('Digite o peso da segunda nota: '))

valorNota = (nota1 * peso1) + (nota2 * peso2)
valorPeso = peso1 + peso2

solucao = valorNota / valorPeso
print('A média ponderada é: ', solucao)

