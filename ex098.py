from time import sleep


def pa(ini,fim,passo):
    print(f'Contagem de {ini} até {fim} de {passo} em {passo}')
    passo=1 if passo==0 else passo
    if ini>fim:
        passo*=-1
        fim-=2
    flag=False
    for c in range(ini,fim+1,passo):
        if flag:
            print(end=' ')
        else: flag=True
        print(c, end='')
        sleep(1/3)
    print(' Fim!\n'+'-='*20)


print('-='*20)
pa(1,10,1)
pa(10,0,2)
print('Agora é sua vez de personalizar a contagem!')
ini= int(input('Início: '))
fim= int(input('Fim: '))
passo= int(input('Passo: '))
pa(ini,fim,passo)