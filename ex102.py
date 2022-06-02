def fat(n=1, show=False):
    fat = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(end=' x ')
            else:
                print(end=' = ')
        fat *= c
    return fat


n = int(input('Qual o número que você quer saber o fatorial? '))
resp = str(input('Você quer mostrar a operação? ')).upper()
show = True if resp in 'SIM' else False
print(fat(n, show))
