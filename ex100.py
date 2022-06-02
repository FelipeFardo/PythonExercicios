from random import randint


def sorteia():
    vetor = []
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(5):
        n = randint(1, 10)
        vetor.append(n)
        print(f'{n} ', end='')
    print('FIM!')
    return vetor


def somaPar(vetor):
    soma = 0
    for c in vetor:
        if c % 2 == 0:
            soma += c
    return soma

    
print(f'A soma dos pares é {somaPar(sorteia())}')
