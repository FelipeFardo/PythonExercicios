preco = float(input('Digite o preco do produto: '))

precoDesconto = preco - preco*5/100

print(f'O produto com 5% de desconto ficará: R$ {precoDesconto:.2f}')
