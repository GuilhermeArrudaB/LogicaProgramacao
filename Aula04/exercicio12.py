"""
Maria quer saber quantos litros de gasolina precisa colocar em seu carro e quanto vai gastar para fazer
uma viagem até a casa de sua irmã.
Dados extras:
- Distância da casa de Maria até sua irmã : 520 km
- Seu carro consome 12 Km/litro de combustível.
- Ela abastece sempre no mesmo posto, onde o preço da gasolina é R$ 4,50 o litro.
Desenvolva um algoritmo onde o usuário digite a distância, o consumo e o valor do litro de
combustível, com estes dados o algoritmo deverá calcular a quantidade de litros de combustível para a
viagem e o custo da viagem.

"""

dist = int(input('Digite a distância em KM para o seu destino: '))
cons = int(input('Digite o consumo do seu veiculo: '))
gas = float(input('Digite o valor do litro da gasolina: '))

litros = dist / cons
valorTotal = litros * gas

print('Para chegar no seu destino o seu carro irá gastar ', round(litros), ' litros de gasolina e gastará ', valorTotal , 'para chegar no destino.')
