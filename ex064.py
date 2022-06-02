valor = soma = 0
cont = -1
while valor != 999:
    soma += valor
    cont += 1
    valor = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')