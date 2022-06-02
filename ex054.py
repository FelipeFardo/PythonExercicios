from datetime import date

anoAtual = date.today().year
cont = 0
for c in range(1, 8):
    anoNascimento = int(input(f'Em que ano a pessoa {c} nasceu ? '))
    idade = anoAtual-anoNascimento
    if idade >= 18:
        cont += 1

print(f'{7-cont} pessoas NÃO atingiram a maioridade')
print(f'{cont} pessoas JÁ atingiram a maioridade')
