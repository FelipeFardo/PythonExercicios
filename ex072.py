numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
'dezesseis', 'dezessete', 'dezoito', 'dezenovo', 'vinte')
numero = int(input('Digite um número entre 0 e 20: '))
while numero>20:
    numero = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'você digitou o {numeros[numero]}')
