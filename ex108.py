from funcoesEx108 import moedas

p = float(input('Digite o preço: R$ '))
porc = float(input('Digite um percentual: (só números) '))
print(f'A metade de {moedas.moeda(p)} é {moedas.moeda(moedas.metade(p))}')
print(f'A dobro de {moedas.moeda(p)} é {moedas.moeda(moedas.dobro(p))}')
print(
    f'Aumentando {porc} % de {moedas.moeda(p)} temos {moedas.moeda(moedas.aumentar(p,porc))}')
print(
    f'Diminuindo {porc} % de {moedas.moeda(p)} temos {moedas.moeda(moedas.diminuir(p,porc))}')
