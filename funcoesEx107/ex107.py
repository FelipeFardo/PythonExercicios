import moedas

p = float(input('Digite o preço: R$ '))
porc = float(input('Digite um percentual: (só números) '))
print(f'A metade de {p} é R$ {moedas.metade(p):.2f}')
print(f'A dobro de {p} é R$ {moedas.dobro(p):.2f}')
print(f'Aumentando {porc}% de {p:.2f} temos R$ {moedas.aumentar(p,porc):.2f}')
print(f'Diminuindo {porc}% de {p:.2f} temos R$ {moedas.diminuir(p,porc):.2f}')
