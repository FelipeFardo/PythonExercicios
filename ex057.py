sexo = str(input('Digite seu sexo: ').strip().upper())
while sexo not in 'MF':
    sexo = str(input('Digite seu sexo novamente: ').strip().upper())
print('Sexo registrado com sucesso. Seu sexo é:', end=' ')
print('MASCULINO' if sexo == 'M' else 'FEMININO')
