from random import randint
cont = 0
while True:
    numeroPc = randint(0, 11)
    numeroJog = int(input('Diga um valor: '))
    jogada = ' '
    total = numeroJog + numeroJog
    while jogada not in 'PI':
        jogada = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {numeroJog} e o computador jogou {numeroPc}')
    if total % 2 == 0 and jogada == 'P' or total % 2 == 1 and jogada == 'I':
        print('Você VENCEU!')
        cont += 1
    else:
        print('Você PERDEU!!')
        break
print(f'Você ganhou {cont} vezes do computador')
