from datetime import date

anoNascimento = int(input('Digite o seu ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual-anoNascimento
print(f'O atleta tem {idade} anos')
print('Categoria: ', end='')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
