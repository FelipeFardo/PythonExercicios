from funcoesEx115a import funcoes

while True:
    opcao = funcoes.menu()
    if opcao == 3:
        funcoes.titulo('SAINDO DO SISTEMA... Até logo')
        break
    else:
        (funcoes.titulo(f'OPÇÃO {opcao}'))

        