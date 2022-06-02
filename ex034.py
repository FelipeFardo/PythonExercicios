salario = float(input('Qual é o salário do funcionário? R$ '))
print(f'Quem ganhava R$ {salario:.2f} passa a ganhar R$ ', end='')

print(f'{salario*1.10:.2f} agora.' if salario >
      1250.00 else f'{salario*1.15:.2f} agora.')
