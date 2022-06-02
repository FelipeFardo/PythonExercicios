def leiaDinheiro(txt):
    while True:
        entrada = input(txt).strip()
        if entrada.replace(',', '').replace('.', '').isnumeric() and entrada.replace(',', '.').count('.') <= 1 and entrada[0] not in ',.' and entrada[len(entrada)-1] not in ',.':
            return float(entrada.replace(',', '.'))
        print(f'ERRO! "{entrada}" é um preço inválido')