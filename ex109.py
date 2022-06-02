from funcoesEx109 import moedas

p = float(input('Digite o preço: R$ '))
porc = float(input('Digite um percentual: (só números) '))
print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p)}')
print(f'A dobro de {moedas.moeda(p)} é {moedas.dobro(p)}')
print(
    f'Aumentando {porc} % de {moedas.moeda(p)} temos {moedas.aumentar(p,porc)}')
print(
    f'Diminuindo {porc} % de {moedas.moeda(p)} temos {moedas.diminuir(p,porc)}')
