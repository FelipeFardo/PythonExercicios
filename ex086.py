matriz = [[], [], []]
for i in range(0, 3):
    for j in range(0, 3):
        num = int(input(f'Digite o valor da Matriz posição {[i+1]}{[j+1]}: '))
        matriz[i].insert(j, num)
print('-='*30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print('')
