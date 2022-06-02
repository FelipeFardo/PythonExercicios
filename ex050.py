soma = 0
cont = 0
for c in range(0, 6):
    numero = int(input(f'Digite o {c+1} número: '))
    if (numero % 2 == 0 and numero != 0):
        cont += 1
        soma += numero
print(f'Valores que são pares: {cont}')
print(f'A soma dos pares é: {soma}')
