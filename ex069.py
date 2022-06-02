print('-'*30)
print('CADASTRE UM PESSOA')
print('-'*30)
tot18 = qtdHomens = qtdMulheres = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        input('Sexo: [M/F] ').strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        qtdHomens += 1
    elif idade < 20:
        qtdMulheres += 1
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print(f'{tot18} pessoas tem mais de 18 anos')
print(f'Existem {qtdHomens} homens')
print(f'Existem {qtdMulheres} mulheres com menos de 20 anos')
