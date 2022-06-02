lista = []
somaIdade = mediaIdade = 0
while True:
    pessoa = {}
    pessoa['nome'] = input('Nome: ')
    sexo = input('Sexo: [M/F] ').upper()
    while sexo not in 'MF' and len(sexo)>0:
        sexo = input('Por favor, digite apenas M ou F.\nSexo: [M/F] ').upper()
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('idade: '))
    lista.append(pessoa)
    resp = input('Você quer continuar? [S/N] ')
    while resp.upper() not in 'SN' and len(resp)>0:
        resp = input(
            'Erro, digite apenas S ou N.\nVocê quer continuar? [S/N] ')
    if resp.upper() in 'NAO':
        break
print('-='*30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
for pessoa in (lista):
    somaIdade+=float(pessoa['idade'])
mediaIdade=somaIdade/len(lista)
print(f'B) A média de idade é de {mediaIdade} anos')
print('C) As mulheres cadastradas foram ', end='')
esp = False
for pessoa in (lista):
    if pessoa['sexo'] == 'F':
        esp=True if esp==False else print(', ',end='')
        print(f'{pessoa["nome"]}', end='')
print('\nD) Lista de pessoas que estão com idade acima da média: ')
for pessoa in lista:
    if pessoa['idade'] > mediaIdade:
        for k,v in pessoa.items():
            print(f'  {k} = {v}; ', end='')
        print('')
print('<< ENCERRADO >>') 