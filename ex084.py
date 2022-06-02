nomePeso = []
pessoa = []
while True:
    nome = (input('Nome: ')).strip()
    peso = float(input('Peso: '))
    nomePeso.append(nome)
    nomePeso.append(peso)
    if len(pessoa) == 0:
        maiorPeso = menorPeso = peso
    else:
        maiorPeso = (maiorPeso + peso + abs(maiorPeso-peso))/2
        menorPeso = (menorPeso + peso - abs(menorPeso-peso))/2
    pessoa.append(nomePeso[:])
    nomePeso.clear()
    resp = ' '
    while resp.upper() not in 'SIMNAO':
        resp = input('Você quer continuar? [S/N] ')
    if resp.upper() in 'NAO':
        break
print(f"Ao todo você cadastrou {len(pessoa)} pessoas")
print(f'O maior peso foi de {maiorPeso} kg. Peso de ', end='')
for i in pessoa:
    if i[1] == maiorPeso:
        print(f'[{i[0]}] ', end='')
print(f'\nO menor peso foi de {menorPeso} kg. Peso de ', end='')
for i in pessoa:
    if i[1] == menorPeso:
        print(f'[{i[0]}] ', end='')
