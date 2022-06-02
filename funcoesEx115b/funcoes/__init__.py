def titulo(txt):
    print('-'*42)
    print(txt.center(42))
    print('-'*42)


def menu(arq):
    while True:
        titulo('MENU PRINCIPAL')
        print("1 - Ver pessoas cadastradas\n2 - Cadastrar nova pessoa\n3 - Sair do sistema\n"+'-'*34)
        try:
            opcao = int(input('Sua opção: '))
            if opcao == 1:
                lerArquivo(arq)
            elif opcao == 2:
                titulo('NOVO CADASTRO')
                nome = str(input('Nome: '))
                idade = leiaInt('Idade: ')
                if not arquivoExiste(arq):
                    criarArquivo(arq)
                cadastrar(arq, nome, idade)
            elif opcao == 3:
                titulo('SAINDO DO SISTEMA... Até logo')
                break
            else:
                print('\033[0;31mERRO! Digite uma opção válida!\033[m')
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Digite um valor inteiro válido\033[m')


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler um arquivo')
    else:
        titulo('PESSOAS CADASTRADAS')
        print(a.read())
    finally:
        a.close()


def leiaInt(txt):
    while True:
        num = input(txt).strip()
        try: 
            int(num)
            return num
        except:
            print('Digite um número inteiro')

def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado')
    finally:
        a.close