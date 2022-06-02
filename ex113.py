def leiaint(txt=''):
    while True:
        try:
            numero = int(input(txt).strip())
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Digite um valor inteiro válido\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[0;31mEntrada de dados interrompida pelo usuário!\033[m')
            return 0
        else:
            return numero


def leiafloat(txt=''):
    while True:
        try:
            numero = float(input(txt).strip())
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Digite um valor real válido\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[0;31mEntrada de dados interrompida pelo usuário!\033[m')
            return 0
        else:
            return numero


numeroInt = leiaint('Digite um número inteiro: ')
numeroReal = leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {numeroInt} e o real foi {numeroReal}')
