def leiaint(txt=''):
    numero = input(txt).strip()
    while not numero.isdigit():
        print('\033[0;31mERRO! Digite um valor inteiro válido\033[m')
        numero = input(txt).strip()
    return int(numero)


numero = leiaint('Digite um número: ')
print(f'Você digitou o valor: {numero}')
