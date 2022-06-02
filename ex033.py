A = int(input('Digite o primeiro valor: '))
B = int(input('Digite o segundo valor: '))
C = int(input('Digite o terceiro valor: '))

W = (A+B-abs(A-B))/2
MENOR = int((W+C-abs(W-C))/2)
X = (A+B+abs(A-B))/2
MAIOR = int((X+C+abs(X-C))/2)
MEIO = A+B+C-MAIOR-MENOR

print(f'O menor valor digitado foi {MENOR}')
print(f'O maior valor digitado foi {MAIOR}')
