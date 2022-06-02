valorCasa = float(input('Qual o valor da casa? '))
salario = float(input('Sálario do comprador? '))
anos = float(input('Quantos anos de financiamento? '))

parcela = valorCasa/(anos*12)

print(f'Para pagar uma casa de R$ {valorCasa:.2f} em {anos} ', end='')
print(f'a prestação será de R$ {parcela:.2f}')

if parcela > salario*0.3:
    print('Empréstimo negado')
else:
    print('Empréstimo concebido')
