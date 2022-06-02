from funcoesEx112.utilidadesCeV import dado, moeda

p = dado.leiaDinheiro('Digite o preço: R$ ')
a = float(input('Digite o aumento: '))
r = float(input('Digite a reducao: '))
moeda.resumo(p, a, r)
