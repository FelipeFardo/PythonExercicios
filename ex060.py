numero = int(input('Digite um número para descobrir o seu fatorial: '))
produto = 1

'''numeroEscolhido=numero
while numero>1:
    produto*=numero
    numero-=1'''


for c in range(1, numero+1):
    produto *= c



print(f'O fatorial de {numero} é igual a {produto}')
