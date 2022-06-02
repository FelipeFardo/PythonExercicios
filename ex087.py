matriz = [[], [], []]
somaPares = somaColuna3 = 0
for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f'Digite o valor da Matriz posição {[i]}{[j]}: ')))
        somaPares += matriz[i][j] if matriz[i][j] % 2 == 0 else 0
        somaColuna3 += matriz[i][j] if j == 2 else 0
print('-=' * 35, *matriz, sep='\n')
print('-='*30, f'\nA soma dos valores da pares é {somaPares}')
print(f'A soma dos valores da terceira coluna é {somaColuna3}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')