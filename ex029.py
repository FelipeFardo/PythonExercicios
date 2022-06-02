velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade>80: 
    valor = (velocidade-80)*7.00
    print('MULTADO! Você excedeu o limite permitido que é de 80 km/h')
    print(f'Você deve pagar uma multa de R${valor:.2f}!')
print('Tenha um bom dia! Dirija com segurança!')
