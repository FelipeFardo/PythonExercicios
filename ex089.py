alunos = []
while True:
   nome = (input('Nome: ')).strip()
   nota1 = float(input('Nota 1: '))
   nota2 = float(input('Nota 2: '))
   media = (nota1+nota2)/2
   alunos.append([nome, [nota1, nota2], media])
   resp = ' '
   while resp.upper() not in 'SIMNAO':
      resp = input('Você quer continuar? [S/N] ')
   if resp.upper() in 'NAO':
      break
print('-='*40, f'{"No.":<4}'+f'{"NOME":<10}' +f'{"MEDIA":>8}', '-'*40, sep='\n')
for c in range(len(alunos)):
    print(f'{c:<4}'+f'{alunos[c][0]:<10}' + f'{alunos[c][2]:>8.1f}')
while True:
    numeroAluno = int(
        input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if numeroAluno == 999:
        break
    if numeroAluno <= len(alunos)-1:
        print(
            f'As notas de {alunos[numeroAluno][0]} são {alunos[numeroAluno][1]}')
print('FINALIZANDO...', '\n<<< VOLTE SEMPRE >>>')