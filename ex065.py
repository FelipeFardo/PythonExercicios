r = 'S'
maior = -999999999999
menor = 99999999
cont = media = soma = 0
while (r == 'S'):
    valor = int(input('Digite um número: '))
    r = str(input('Você quer continuar [S/N]: ')).upper()
    maior = (maior+valor+abs(maior-valor))/2
    menor = (menor+valor-abs(menor-valor))/2
    soma += valor
    cont += 1
    while (r != 'S' and r != 'N'):
        print('Resposta inválida')
        r = str(input('Você quer continuar [S/N]: ')).upper()
media = soma/cont
print(f'Você digitou {cont} números e a média entre eles é {media}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
