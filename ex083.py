expr = input('Digite a expressão: ')
pilha = []
for carac in expr:
    if carac == '(':
        pilha.append('(')
    elif carac == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está VÁLIDA!')
else:
    print('Sua expressão está errada!')
