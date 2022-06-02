soma = cont = 0
while True:
    valor = int(input('Digite um número [999 para parar]: '))
    if valor == 999:
        break
    soma += valor
    cont += 1
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')
