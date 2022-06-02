diasAlugados = int(input('Quantos dias alugados? '))
kmRodados = float(input('Quantos km rodados? '))

valor = 60*diasAlugados + kmRodados*0.15
print(f'O total a pagar é R$ {valor:.2f}')
