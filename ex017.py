from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimeito do cateto adjacente: '))
hi = hypot(co,ca)
print(f'A hipotenusa vai medir {hi:.2f}')