tabelaBrasileirao = ('Corinthians', 'Atlético-MG', 'São Paulo', 'Botafogo',
                     'Santos', 'Coritiba', 'Avaí', 'América-MG', 'Palmeiras', 'Bragantino',
                     'Internacional', 'Fluminense', 'Goiás', 'Cuiabá', 'Athletico-PR', 'Flamengo',
                     'Juventude', 'Ceará SC', 'Atlético-GO', 'Fortaleza',)

print('Os 5 primeiros colocados do Brasileirão 2022 foram: ')
for c in range(0, 5):
    print(f'{c+1} lugar: {tabelaBrasileirao[c]}')

print('Os 4 ultimos colocados do Brasileirão 2022 foram: ')
for c in range(16, 20):
    print(f'{c+1} lugar: {tabelaBrasileirao[c]}')

print('Times em ordem alfabética: ')
print(sorted(tabelaBrasileirao))
print('O Flamengo está na posição')
print(tabelaBrasileirao.index('Flamengo')+1)
