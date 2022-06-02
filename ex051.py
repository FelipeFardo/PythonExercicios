print('='*40)
print(' '*10+'10 TERMOS DE UMA P.A.')
print('='*40)

a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
print(f'{a1}', end='')
for c in range(1, 11):
    print(f' -> {a1+(c*r)} ', end='')
