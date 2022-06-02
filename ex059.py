sair = False
op = 3
while sair == False:
    valor1 = float(input('Digite o primeiro valor: '))
    valor2 = float(input('Digite o segundo valor: '))
    while 1 <= op and op <= 5:
        print('='*10 + ' Menu '+'='*10)
        op = int(input('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS VALORES
    [ 5 ] SAIR DO PROGRAMA
>>>>>>Escolha uma operação e digite seu valor: \n'''))
        while 5 < op or op < 1:
            print('='*10+'Menu'+'='*10)
            op = int(input('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS VALORES
    [ 5 ] SAIR DO PROGRAMA
>>>>>>Escolha uma operação válida e digite seu valor: \n'''))
        if op == 1:
            soma = valor1 + valor2
            print(f'A soma é: {soma}\n')
        elif op == 2:
            produto = valor1 * valor2
            print(f'O produto é: {produto}\n')
        elif op == 3:
            maior = (valor1 + valor2 + abs(valor1 - valor2))/2
            print(f'O maior é: {maior}\n')
        elif op == 5:
            op = 6
            sair = True
        else:
            valor1 = float(input('Digite o primeiro valor: '))
            valor2 = float(input('Digite o segundo valor: '))
