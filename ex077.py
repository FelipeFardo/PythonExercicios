palavras = ('Aprender', 'Programar', 'Linguagem', 'Python',
            'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar',
            'Mercado', 'Programador', 'Futuro')

for palavra in palavras:
    print(f'Na palavra {palavra.upper()} temos', end='')
    for pos in palavra:
        if pos.lower() in 'aeiou':
            print(f' {pos.lower()}', end='')
    print('')