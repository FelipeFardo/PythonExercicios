
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1+n2)/2

if media >=7:
    print('Aluno aprovado')
elif media <5:
    print('Aluno reprovado')
else:
    print('Aluno em recuperação')