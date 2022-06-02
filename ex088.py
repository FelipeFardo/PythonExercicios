from random import sample
from time import sleep
lista = []
print(f'-'*31, '       JOGA NA MEGA SENA', f'-'*31, sep='\n')
for c in range(int(input('Quantos jogos você quer que eu sorteie? '))):
    lista.append(sorted((sample(range(1, 61), 6))[:]))
    print(f'Jogo {c+1}: {lista[c]}')
    sleep(1/2)
print('-='*5, '< BOA SORTE! >', '-='*5)