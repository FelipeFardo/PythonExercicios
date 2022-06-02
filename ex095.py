time = []
while True:
    jogador = {}
    gols = []
    jogador['nome'] = input('Nome de um jogador: ')
    part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range (0,part):
        gols.append(int(input(f'Quantos gols na partida {i+1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador)
    resp = input('Você quer continuar? [S/N] ')
    while resp.upper() not in 'SN' and len(resp)>0:
        resp = input('Erro, digite apenas S ou N.\nVocê quer continuar? [S/N] ')
    if resp.upper() in 'NAO':
        break
    print('-='*40)
print('-='*40, f'{"COD.":<6}'+f'{"NOME":<15}' +f'{"GOLS":<15}'+f'{"TOTAL":<15}', '-'*40, sep='\n')
for k,v in enumerate(time):
    print(f'{k:>3}   ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca==999:
        break
    if busca>= len(time):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f'  -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i,g in enumerate(time[busca]["gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<< VOLTE SEMPRE >>')