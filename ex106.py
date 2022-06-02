c = ('\033[m',         # 0 - sem cores
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[7;30m',     # 6 - branco
     )


def titulo(txt, cor=0):
    print(c[cor], end='')
    print('~'*(len(txt)+6))
    print(' '*3 + txt + ' '*3)
    print('~'*(len(txt)+6))
    print(c[0], end='')


def ajuda(comand):
    titulo(f'Acessando o manual do comand \'{comand}\'', 4)
    print(c[6], end='')
    help(comand)
    print(c[0], end='')


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comand = input('Função ou biblioteca > ').lower()
    if comand == 'fim':
        break
    ajuda(comand)
titulo('ATÉ LOGO', 1)
