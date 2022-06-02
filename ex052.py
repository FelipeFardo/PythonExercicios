n = int(input('Digite um número: '))
cont = 0
for c in range(1, n+1, 1):
    if (n % c == 0):
        cont += 1
        print(f'\033[33m{c}', end=' ')
    else:
        print(f'\033[31m{c}', end=' ')
print('')
print(f'O número {n} foi divisível {cont} vezes')

if cont == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele NÃO é PRIMO')
