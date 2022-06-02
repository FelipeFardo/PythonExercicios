print('='*40)
print(' '*10+'10 TERMOS DE UMA P.A.')
print('='*40)

a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 0
flag = maisTermo = True
termosMostrados = 10
while c < 10:
    if (flag):
        flag = False
    else:
        print(' -> ', end='')
    print(f'{a1+(c*r)}', end='')
    c += 1
qntTermos = int(input('\nVocê que saber mais quantos termos? '))
while qntTermos != 0:
    termosMostrados += qntTermos
    qntTermos += c
    flag = True
    while c < qntTermos:
        if (flag):
            flag = False
        else:
            print(' -> ', end='')
        print(f'{a1+(c*r)}', end='')
        c += 1
    qntTermos = int(input('\nVocê que saber mais quantos termos? '))

print(f'Progressão finalizada foram mostrados {termosMostrados} termos')
