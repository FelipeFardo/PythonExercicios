maiorIdade = -1
nomeMaiorIdade = ''
soma = 0
media = 0.0
contMulher = 0
for c in range(1, 5):
    print('-'*5+f' {c}ª PESSOA '+'-'*5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    soma += idade
    if sexo in 'Mm':
        maiorIdade = int((maiorIdade+idade+abs(maiorIdade-idade))/2)
        if idade == maiorIdade:
            nomeMaiorIdade = nome
    if sexo in 'fF' and idade < 20:
        contMulher += 1
media = soma/4
print(f'A média de idade do grupo é: {media}')
print(f'{nomeMaiorIdade} tem {maiorIdade}é o homem mais velho')
print(f'{contMulher} mulheres tem menos 20 anos')
