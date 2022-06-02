from time import sleep
from random import randint
dicio = {}
lista = []
print('Valores sorteados: ')
for c in range(1, 5):
    dicio['jogador'] = str((f'Jogador{c}'))
    dicio['pontos'] = int(randint(1, 6))
    lista.append(dicio.copy())
    print(f'{dicio["jogador"]} tirou {dicio["pontos"]} no dado.')
    sleep(1/2)
print('-='*30, '  '+'== RANKING DOS JOGADORES == '+'  ', sep='\n')
rank = 1
for c in range(6, 0, -1):
    for i in lista:
        if i['pontos'] == c:
            print(f'   {rank}° lugar: {i["jogador"]} com {c}.')
            rank += 1
            sleep(1/2)