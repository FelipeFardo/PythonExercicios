from random import _inst, randint
itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)

jogador = int(input('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
Qual é a sua jogada? '''))

print(f'Jogada do computador: {itens[computador]}')
if jogador > 2 or jogador < 0:
    print('Jogada Inválida')
else:
    if computador == 0:
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('VOCÊ VENCEU!')
        else:
            print('COMPUTADOR VENCEU!')
    elif computador == 1:
        if jogador == 0:
            print('COMPUTADOR VENCEU')
        elif jogador == 1:
            print('EMPATE')
        else:
            print('VOCÊ VENCEU!')
    elif computador == 2:
        if jogador == 0:
            print('VOCÊ VENCEU!')
        elif jogador == 1:
            print('COMPUTADOR VENCEU')
        else:
            print('EMPATE')
