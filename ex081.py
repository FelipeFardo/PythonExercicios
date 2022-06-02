lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp.upper() not in 'SIMNAO':
        resp = input('Você quer continuar? [S/N] ')
    if resp.upper() in 'NAO':
        break
lista.sort(reverse=True)
print('-='*40)
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 NÃO foi encontrado na lista!')
