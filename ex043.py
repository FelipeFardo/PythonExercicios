
peso= float(input('Qual é o seu peso? (kg) '))
altura= float(input('Qual é a sua altura? (m) '))

IMC = peso/(altura**2)

print (f'Seu IMC é {IMC} e você está: ', end='')
if IMC<18.5:
    print('Abaixo do Peso')
elif IMC<25:
    print('Peso Ideal')
elif IMC<30:
    print('Sobrepeso')
elif IMC<40:
    print('Obesidade')
else:
     print('Obesidade Mórbida')