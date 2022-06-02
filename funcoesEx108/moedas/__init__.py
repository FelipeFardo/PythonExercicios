def metade(n=0):
    resp = (n/2)
    return resp


def dobro(n=0):
    resp = (n*2)
    return resp


def aumentar(n=0, p=0):
    resp = (n+n*p/100)
    return resp


def diminuir(n=0, p=0):
    resp = (n-n*p/100)
    return resp


def moeda(preco=0, moeda='R$'):
    return f'{moeda} {preco:>.2f}'.replace('.', ',').strip()
