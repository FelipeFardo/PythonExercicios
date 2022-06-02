print('='*40)
print(' '*10+'10 TERMOS DE UMA P.A.')
print('='*40)

a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 0
flag = True
while c < 10:
    if (flag):
        flag = False
    else:
        print(' -> ', end='')
    print(f'{a1+(c*r)}', end='')
    c += 1
