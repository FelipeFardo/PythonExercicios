frase = input('Digite seu nome completo: ').strip()
nome = frase.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}')

print('Seu ultimo nome é', nome[len(nome)-1])
