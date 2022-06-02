from random import randint

numeroEscolhido = int(input('Em que número eu pensei? '))
numeroSorteado = randint(0, 5)

if numeroEscolhido == numeroSorteado:
    print('Parabéns, você acertou o número sorteado')
else:
    print(f'Você errou o número sorteado, não era o {numeroEscolhido} e sim {numeroSorteado}')
