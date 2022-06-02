from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
print(f'O ano {ano} é ', end='')

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('BISSEXTO')
else:
    print('NÃO É BISSEXTO')
