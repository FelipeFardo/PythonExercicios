lista = []

while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor já está contido na lista!')
    resp = ' '
    while resp.upper() not in 'SIMNAO':
        resp = input('Você quer continuar? [S/N] ')
    if resp.upper() in 'NAO':
        break
lista.sort()
print('-='*40)
print(f'Você digitou os valores {lista}')
