numero = int(input('Me diga um número qualquer: '))

print(f'O número {numero} é ', end="")
print('PAR' if numero % 2 == 0 else 'ÍMPAR')