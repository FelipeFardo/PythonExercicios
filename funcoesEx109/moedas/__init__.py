def metade(n=0, form=True):
    resp = (n/2)
    return moeda(resp) if form else resp


def dobro(n=0, form=True):
    resp = (n*2)
    return moeda(resp) if form else resp


def aumentar(n=0, p=0, form=True):
    resp = (n+n*p/100)
    return moeda(resp) if form else resp


def diminuir(n=0, p=0, form=True):
    resp = (n-n*p/100)
    return moeda(resp) if form else resp


def moeda(preco=0, moeda='R$'):
    return f'{moeda} {preco:>.2f}'.replace('.', ',')
