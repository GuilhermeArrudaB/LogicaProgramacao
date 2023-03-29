"""
Escrever um algoritmo para ler uma temperatura em Fahrenheit e apresentá-la convertida em graus
Centígrados.
(Fahrenheit – 32) x 5
Fórmula: Centígrados = ----------------------------
9

"""

F = float(input('Digite a temperatura em Fahrenheit para conversão: '))

C = (F - 32) * 5/9

print('Convertido para Celsius:', C)
