from datetime import date
anoNascimento = int(input('Qual ano você nasceu? '))
anoAtual= date.today().year
idade = anoAtual-anoNascimento

print(f'Quem nasceu em {anoNascimento} tem {idade} anos em {anoAtual}')
if idade==18:
    print('Está no ano de você se alistar!')
elif idade>18:
    print(f'Você deveria ter se alistado há {idade-18} anos')
else: 
    print(f'Você deverá se alistar daqui a {18-idade} anos')