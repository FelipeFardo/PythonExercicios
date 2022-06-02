num = (int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),
       int(input('Digite um valor: ')))

print(f'Você digitou os valores {num}')
print(f'O número nove aparece {num.count(9)} vezes na tupla')
if 3 in num:
    print(f'O valor 3 apareceu na posição {num.index(3)+1}')
else:
    print('O valor 3 não apareceu em nenhuma posição')
print('Os valores parem foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end='')
