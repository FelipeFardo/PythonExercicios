valor = int(input('Que valor você deseja sacar? '))
auxValor = valor
nota50 = int(auxValor/50)
auxValor %= 50
nota20 = int(auxValor/20)
auxValor %= 20
nota10 = int(auxValor/10)
auxValor %= 10
nota1 = int(auxValor)
print(f'Sacando R$ {valor:.2f}')
if nota50 > 0:
    print(f'Total de {nota50} cédulas de R$ 50')
if nota20 > 0:
    print(f'Total de {nota20} cédulas de R$ 20')
if nota10 > 0:
    print(f'Total de {nota10} cédulas de R$ 10')
if nota1 > 0:
    print(f'Total de {nota1} cédulas de R$ 1')
