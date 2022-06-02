numero = int(input('Digite um número: '))
uni = numero % 10
dez = numero//10 % 10
cent = numero//100 % 10
mil = numero//1000 % 10

print(f'Analisando o número {numero}')
print(f'Unidade: {uni}')
print(f'Dezena: {dez}')
print(f'Centena: {cent}')
print(f'Milhar: {mil}')