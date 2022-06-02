lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print(f'Você digitou os valores {lista}')

print(f'O MAIOR valor digitado foi {max(lista)} nas posições ', end='')
for c in range(0, len(lista)):
    if lista[c] == max(lista):
        print(f'{c}...', end=' ')

print(f'\nO MENOR valor digitado foi {min(lista)} nas posições ', end='')
for c in range(0, len(lista)):
    if lista[c] == min(lista):
        print(f'{c}...', end=' ')