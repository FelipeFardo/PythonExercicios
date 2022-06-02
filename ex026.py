frase = input('Digite uma frase: ').upper().strip()
print('A letra A aparece', frase.count('A'), 'vezes na frase.')
print('A primeira letra A aparece na posicao', frase.find('A')+1)
print('A ultima letra A aparece na posicao', frase.rfind('A')+1)
