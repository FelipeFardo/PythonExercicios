maior = -1.00
menor = 1000.00

for c in range(1, 6):
    numero = float(input(f'Digite o peso da pessoa {c}: '))
    menor = float((numero+menor-abs(numero-menor))/2)
    maior = float((maior+numero+abs(maior-numero))/2)

print(f'O maior peso foi {maior:.2f} kg e o menor peso foi {menor:.2f} kg')
