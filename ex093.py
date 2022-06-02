jogador = {}
gols = []
jogador['nome'] = input('Nome de um jogador: ')
part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for i in range (0,part):
    gols.append(int(input(f'Quantos gols na partida {i}? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i,v in enumerate (jogador['gols']):
    print(' '*5+f' => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
print('-='*30)