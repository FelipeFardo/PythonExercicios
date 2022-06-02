soma = 0;cont = 0
for c in range(3, 501, 3):
    if (c % 2 != 0):
        cont += 1
        soma += c
print (f'Valores solicitados: {cont}')
print(f'A soma é: {soma}')
