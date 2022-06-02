def resumo(p=0, a=0, r=0):
    escreva('RESUMO DO VALOR')
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{moeda(dobro(p))}')
    print(f'Metade do preço \t{moeda(metade(p))}')
    print(f'{a} % de aumento: \t{moeda(aumento(p,a))}')
    print(f'{r} % de redução: \t{moeda(reducao(p,r))}')
    print('-'*30)


def escreva(txt):
    print('-'*30)
    print(txt.center(30))
    print('-'*30)


def dobro(p):
    return p*2


def metade(p):
    return p/2


def aumento(p, a):
    return p*(1 + a/100)


def reducao(p, a):
    return p*(1 - a/100)


def moeda(preco=0, moeda='R$'):
    return str(f'{moeda}{preco:>.2f}'.replace('.', ','))
