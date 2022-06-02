def titulo(txt):
    print('-'*42)
    print(txt.center(42))
    print('-'*42)


def menu():
    titulo('MENU PRINCIPAL')
    print("1 - Ver pessoas cadastradas\n2 - Cadastrar nova pessoa\n3 - Sair do sistema\n"+'-'*34)
    while True:
        try:
            opcao = int(input('Sua opção: '))
            if 0 < opcao < 4:
                return opcao
            else:
                print('\033[0;31mERRO! Digite uma opção válida!\033[m')
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Digite um valor inteiro válido\033[m') 