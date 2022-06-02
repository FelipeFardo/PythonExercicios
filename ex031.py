distancia = float(input('Qual é a distância da sua viagem? '))
print(f"""Você está preste  a comerçar uma viagem de {distancia:.1f} km
E o preço de sua passagem será de R$ """, end='')
print(f'{distancia/2:.2f}' if distancia <= 200.00 else f'{distancia*0.45:.2f}')
