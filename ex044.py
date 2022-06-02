preco = float(input('Qual o preço as compras? '))
opcao = int(input('''Formas de pagamento
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] em até 2x no cartão
[4] 3x ou mais no cartão
Qual é a opção '''))

if opcao > 4 or opcao < 1:
    print('Escolha uma opção válida')
else:
    if opcao == 1:
        valorFinal = preco*0.9
    elif opcao == 2:
        valorFinal = preco*0.95
    elif opcao == 3:
        valorFinal = preco
        print(f'Sua compra será parcelada em 2x de {valorFinal/2:.2f} SEM JUROS')
    else:
        valorFinal = preco*1.2
        parcelas=int(input('Quantas parcelas? '))
        print(f'Sua compra será parcelada em 3x de {valorFinal/parcelas:.2f} COM JUROS')
    print(f'Sua compra de R$ {preco:.2f} vai custar R$ {valorFinal:.2f} no final')
