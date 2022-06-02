def maior(*num):
    maior = 0
    cont = False
    print('-='*20+'\nAnalisando os valores passados...')
    for valor in num:
        if cont == True:
            print(end=' ')
        print(f'{valor}', end='')
        maior = (maior+valor+abs(maior-valor))/2 if cont else valor
        cont = True
    print(
        f'\nForam informados {len(num)} valores ao todo.\nO maior valor foi {int(maior)}')


maior(0, 2, 3, 4, 23, 654, 32, 544, 7653, -1, 43)
