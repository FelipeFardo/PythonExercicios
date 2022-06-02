from random import randint

numeroEscolhido = int(input('Em que número eu pensei? '))
numeroSorteado = randint(0, 10)
palpite = 1
while numeroEscolhido != numeroSorteado:
    numeroEscolhido = int(input('Você errou, tento novamente! Em que número eu pensei? '))
    palpite += 1
print(f'Parabéns, você acertou o número sorteado! Foram necessários {palpite} palpites!')
