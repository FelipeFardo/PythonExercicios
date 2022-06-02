lista = list()
pares = list()
impares = list()

while True:
    lista.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp.upper() not in 'SIMNAO':
        resp = input('Você quer continuar? [S/N] ')
    if resp.upper() in 'NAO':
        break
for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print('-='*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista impares é {impares}')
