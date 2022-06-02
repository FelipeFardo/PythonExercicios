def area(a,b):
    area= a*b
    return area

print('  CONTROLE DE TERRENO')
print('-'*15)
a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
print(f'A área de um terreno de {a} x {b} é de {area(a,b):.2f} m²')