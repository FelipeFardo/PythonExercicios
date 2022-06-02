valorTotal = 0
qtd1000 = 0
while True:
    nome = input('Digite o nome do produto: ')
    preco = int(input('Digite o preco do produto: '))
    valorTotal += preco
    if valorTotal == preco or preco < menorPreco:
        menorPreco = preco
        nomeMenorPreco = nome
    if preco > 1000:
        qtd1000 += 1
    resp = ' '
    while resp not in 'SN':
        resp = input('Você quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N': 
        break
print(f'O total da compra foi R$ {valorTotal:.2f} ')
print(f'Há {qtd1000} produtos custando mais de R$ 1000,00')
print(f'O produto mais barato foi {nomeMenorPreco} que custa {menorPreco}')
