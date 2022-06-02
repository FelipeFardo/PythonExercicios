while True:
    valor = int(input('Digite um número para ver sua tabuada: '))
    if valor < 0:
        break
    for c in range(1, 11):
        print(f'{c:2} x {valor} = {valor*c:2}')

