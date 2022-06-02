aluno = {}
aluno['nome'] = input('Nome: ')
aluno['nota'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['nota'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['nota'] <= 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('-='*30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
